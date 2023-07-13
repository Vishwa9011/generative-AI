from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
import openai
import json
import os

# Enable CORS for all routes

if __name__ == '__main__':
    os.environ['FLASK_ENV'] = 'development'
    os.environ['FLASK_DEBUG'] = '1'


app = Flask(__name__)

CORS(app)


def load_data():
    with open("data.json", 'r') as f:
        data = json.load(f)
    return data


def save_data(json_data):
    with open("data.json", 'w') as f:
        json.dump(json_data, f)


@app.route("/")
def Home():
    data = jsonify(load_data())
    return data


@app.route("/dishes")
def dishes():
    data = load_data()
    return data['dishes']


@app.route("/create", methods=["POST"])
def create():
    json_data = load_data()
    data = request.get_json()
    print(f'data {data}')
    json_data['dishes'].append(data)
    save_data(json_data)
    return f"Congratulations Form has been submitted"


@app.route('/update/<string:id>', methods=['POST'])
def update(id):
    json_data = load_data()
    data = list(filter(lambda dish: dish["id"] == id, json_data['dishes']))
    if data and data[0].get('name'):
        client_data = request.get_json()
        for i, dish in enumerate(json_data['dishes']):
            if dish['id'] == id:
                json_data['dishes'][i] = client_data
                save_data(json_data)
                return 'Data has been updated successfully.'
        return 'Entry not found for the given ID.'
    return 'Invalid data or name is missing.'


@app.route('/delete/<string:id>', methods=['DELETE'])
def delete(id):
    data = load_data()
    for dish in data[:]:
        if dish['id'] == id:
            data.remove(dish)
            return 'Id has been deleted successfully'
    return 'Id not found'


# -----------Order----------

@app.route("/orders")
def orders():
    data = load_data()
    return data['orders']


@app.route("/neworder", methods=["POST"])
def createOrder():
    json_data = load_data()
    data = request.get_json()
    print(f'data {data}')
    json_data['orders'].append(data)
    save_data(json_data)
    return f"Congratulations Form has been submitted"


@app.route('/updateorder/<string:id>', methods=['POST'])
def updateOrder(id):
    json_data = load_data()
    data = list(filter(lambda order: order["id"] == id, json_data['orders']))
    if data and data[0].get('id'):
        client_data = request.get_json()
        for i, order in enumerate(json_data['orders']):
            if order['id'] == id:
                json_data['orders'][i]["status"] = client_data["status"]
                save_data(json_data)
                return 'Data has been updated successfully.'
        return 'Entry not found for the given ID.'
    return 'Invalid data or name is missing.'


# Open AI Chat Assistance with the help of ChatGPT
openai.api_key = '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'


@app.route('/query', methods=['POST'])
def process_query():
    data = request.get_json()
    user_message = data['query']
    conversation_history = [
        {
            'role': 'system',
            'content': 'You are a helpful assistant.'
        },
        {
            'role': 'user',
            'content': user_message
        }
    ]
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            messages=conversation_history,
            temperature=0.9,
            max_tokens=100,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.6,
            stop=None
        )
        answer = response.choices[0].message['content'].strip()
        return jsonify({'answer': answer})
    except Exception as e:
        print("Error:", e)
        return {"answer": "An error occurred"}


if __name__ == '__main__':
    app.run(port=8000)
