from flask_socketio import SocketIO, emit
from flask import Flask, request, make_response, jsonify
from pymongo import MongoClient
from bson import ObjectId
import openai
import uuid

app = Flask(__name__)
socketio = SocketIO(app)
openai.api_key = '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'
client = MongoClient("mongodb+srv://abha25meshram:Foodify@cluster0.siiwyju.mongodb.net/Foodify?retryWrites=true&w=majority")
db = client["Foodify"]
menu_collection = db["menu"]
orders_collection = db["orders"]
feedback_collection = db["feedback"]

menu = []
orders = []
order_id_counter = 1

#---------------------------------------------chatbot--------------------------------

@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_message = request.json['message']
    response = openai.Completion.create(
        engine='davinci',  
        prompt=f'User: {user_message}\nChatbot:',
        max_tokens=50,  
        temperature=0.7, 
        n=1,
        stop=None
    )
    chatbot_response = response.choices[0].text.strip()

    return jsonify({'response': chatbot_response})

#-----------------------------------------SocketIO----------------------------------

# @socketio.on('order_status_update')
# def handle_order_status_update(data):
#     order_id = data['order_id']
#     new_status = data['new_status']
#     emit('order_status_update', {'order_id': order_id, 'new_status': new_status}, broadcast=True)

# {
# "event": "order_status_update", 
# "data": {"order_id": 123, 
#           "new_status": "Completed"}
# }

@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*" 
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"  
    response.headers["Access-Control-Allow-Headers"] = "Content-Type" 
    return response

@app.after_request
def apply_cors_headers(response):
    return add_cors_headers(response)

#---------------------------------------Home page--------------------------------
    
@app.route('/',methods=["GET"]) 
def index():
    response = make_response('Welcome Foodies in Foodify!')
    response.status_code = 200
    return response

#--------------------------------------- GET Menu --------------------------------

@app.route("/menu", methods=["GET"])
def get_menu():
    menu_data = menu_collection.find_one()
    if menu_data:
        return jsonify(menu_data.get("menu", []))
    else:
        return jsonify([])
    
 #--------------------------------------- GET Orders --------------------------------   
    
@app.route("/orders", methods=["GET"])
def review_orders():
    try:
        orders_data = list(orders_collection.find())
        if orders_data:
            for order in orders_data:
                order["_id"] = str(order["_id"])
            return jsonify(orders_data)
        else:
            return "No orders found", 404
    except Exception as e:
        return f"Error retrieving orders: {str(e)}", 500

#------------------------------------------AddItem POST------------------------------

@app.route("/add", methods=["POST"])
def add_dish():
    dish = request.get_json()
    menu.append(dish)
    save_data()
    menu_collection.replace_one({}, {"menu": menu}, upsert=True)
    return "Dish added to the menu."

# {
#   "dish_id":2,
#   "dish_name":"idli",
#   "price":40,
#   "availability":"no"
# }

#----------------------------------------Menu/id  DELETE----------------------------------------

@app.route("/menu/<dish_id>", methods=["DELETE"])
def remove_dish(dish_id):
    for dish in menu:
        if dish["dish_id"] == int(dish_id):
            menu.remove(dish)
            save_data()
            return "Dish removed from the menu."
    return "Dish not found in the menu."


#--------------------------------------Menu/id PUT ----------------------------- 

@app.route("/menu/<dish_id>", methods=["PUT"])
def update_availability(dish_id):
    for dish in menu:
        if dish["id"] == dish_id:
            dish["availability"] = not dish["availability"]
            save_data()
            return "Availability updated."
    return "Dish not found in the menu."


#-------------------------------------------POST orders--------------------------
def generate_unique_order_id():
    # Generate a UUID as a unique order ID
    return str(uuid.uuid4())

@app.route("/orders", methods=["POST"])
def take_order():
    order = request.get_json()
    dish_ids = order.get("dish_ids", [])
    person_name = order.get("person_name") 
    ordered_dishes = []
    total_price = 0

    if not dish_ids:
        return "No dish IDs provided.", 400

    for dish_id in dish_ids:
        valid_dish = False
        dish = menu_collection.find_one({"dish_id": dish_id, "availability": "yes"})
        if dish:
            ordered_dishes.append(dish)
            total_price += dish["price"]
            valid_dish = True

        if not valid_dish:
            return f"Invalid dish ID: {dish_id} or dish is not available.", 400

    order_data = {
        "id": generate_unique_order_id(),
        "dishes": ordered_dishes,
        "person_name": person_name,
        "status": "Received",
        "total_price": total_price,
        "feedback": "",
        "feedback_given": False
    }

    orders_collection.insert_one(order_data)
    socketio.emit('new_order', order_data, broadcast=True)

    return "Order placed successfully."


@app.route("/orders/<int:order_id>/feedback", methods=["POST"])
def submit_feedback(order_id):
    order = next((o for o in orders if o["id"] == order_id), None)
    if order:
        if order["status"] == "Delivered" and not order["feedback_given"]:
            feedback = request.get_json().get("feedback")
            if feedback:
                order["feedback"] = feedback
                order["feedback_given"] = True

                # Emit a Socket.IO event to notify clients about the new feedback
                socketio.emit('new_feedback', {"order_id": order_id, "feedback": feedback}, broadcast=True)

                return "Feedback submitted."
            else:
                return "Feedback not provided.", 400
        else:
            return "Feedback can only be submitted for delivered orders and if feedback hasn't been given before.", 400
    else:
        return "Order not found.", 404


@socketio.on('order_status_update')
def handle_order_status_update(data):
    order_id = data['order_id']
    new_status = data['new_status']

    # Update the order status
    for order in orders:
        if order["id"] == order_id:
            order["status"] = new_status
            break

    # If the status is "Delivered," emit a Socket.IO event to notify clients to allow feedback submission
    if new_status == "Delivered":
        socketio.emit('allow_feedback_submission', {"order_id": order_id}, broadcast=True)

    # Emit a Socket.IO event to notify clients about the updated order status
    socketio.emit('order_status_updated', {"order_id": order_id, "new_status": new_status}, broadcast=True)

#------------------------------------------------------------------------------------------------

# @app.route("/orders/<int:order_id>", methods=["PUT"])
# def update_order_status(order_id):
#     status_choice = request.get_json()["status"]
#     order = orders_collection.find_one({"orders.id": order_id})

#     if order:
#         for item in order["orders"]:
#             if item["id"] == order_id:
#                 break
#         orders_collection.replace_one({"orders.id": order_id}, order)
#         socketio.emit('order_status_update', {'order_id': order_id, 'new_status': status_choice}, broadcast=True)

#         return "Status updated."
#     else:
#         return "Order not found."
    


# @socketio.on('update_order_status')
# def handle_update_order_status(data):
#     order_id = data['order_id']
#     new_status = data['new_status']  
#     if new_status == 'Delivered':
#         socketio.emit('show_feedback_form', {'order_id': order_id}, broadcast=True)

# @app.route("/orders/<int:order_id>", methods=["PUT"])
# def update_order_status(order_id):
#     request_data = request.get_json()
#     new_status = request_data["status"]
#     order = orders_collection.find_one({"orders.id": order_id})

#     if order:
#         for item in order["orders"]:
#             if item["id"] == order_id:
#                 item["status"] = new_status
#                 if new_status == "Delivered":
#                     item["feedback_given"] = False  
#                 break

#         orders_collection.replace_one({"orders.id": order_id}, order)
#         socketio.emit('order_status_update', {'order_id': order_id, 'new_status': new_status}, broadcast=True)

#         return "Status updated."
#     else:
#         return "Order not found."



# @app.route("/orders/<int:order_id>/feedback", methods=["POST"])
# def submit_feedback(order_id):
#     request_data = request.get_json()
#     feedback = request_data.get("feedback")

#     if feedback is None:
#         return "Feedback not provided."

#     order = orders_collection.find_one({"orders.id": order_id})

#     if order and order.get("feedback_given") == False:
#         for item in order["orders"]:
#             if item["id"] == order_id:
#                 item["feedback"] = feedback
#                 item["feedback_given"] = True
#                 break

#         orders_collection.replace_one({"orders.id": order_id}, order)

#         order_id_str = str(order_id)

#         emit('new_feedback', {'order_id': order_id, 'feedback': feedback}, broadcast=True)

#         return jsonify({"order_id": order_id_str, "message": "Feedback submitted."})
#     else:
#         return "Order not found or feedback already given."
    

    #-------------------------------------------------------------------------------    

# @socketio.on('submit_feedback')
# def handle_submit_feedback(data):
#     order_id = data['order_id']
#     feedback = data['feedback']

#     # Handle the feedback logic
#     order = orders_collection.find_one({"orders.id": order_id})
#     if order and not order.get("feedback_given"):
#         for item in order["orders"]:
#             if item["id"] == order_id:
#                 item["feedback"] = feedback
#                 item["feedback_given"] = True
#                 break

#         orders_collection.replace_one({"orders.id": order_id}, order)

#         # Emit a Socket.IO event to notify other clients about the new feedback
#         socketio.emit('new_feedback', {'order_id': order_id, 'feedback': feedback}, broadcast=True)


#------------------------------------------orders/status GET------------------------------------------

@app.route("/orders/<status_choice>", methods=["GET"])
def filter_orders_by_status_choice(status_choice):
    filtered_orders = [order for order in orders if order["status"].lower() == status_choice.lower()]
    return jsonify(filtered_orders)



#-------------------------------------------LOAD DATA--------------------------------

def load_data():
    global menu, orders, order_id_counter

    menu_data = menu_collection.find_one()
    if menu_data:
        menu = menu_data.get("menu", [])

    orders_data = orders_collection.find_one()
    if orders_data:
        orders = orders_data.get("orders", [])

    order_id_counter = len(orders)

#--------------------------------------------SAVE DATA  ---------------------------


def save_data():
    menu_data = {"menu": menu}
    menu_collection.replace_one({}, menu_data, upsert=True)

    orders_data = {"orders": orders}
    orders_collection.replace_one({}, orders_data, upsert=True)



if __name__ == "__main__":
    load_data()
    app.run()
    socketio.run(app)
