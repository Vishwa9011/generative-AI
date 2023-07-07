from flask import Flask, request, json, jsonify, render_template
import os
import uuid


app = Flask(__name__)


def load_data():
    with open("data.json", 'r') as f:
        data = json.load(f)
        return data


def save_data(new_json_data):
    with open('data.json', 'w')as f:
        json.dump(new_json_data, f)


@app.route("/")
def home():
    data = load_data()
    print(data)
    # return 'home'
    return render_template('home.html')


@app.route("/add-dish", methods=['GET', 'POST'])
def add_dish():
    json_data = load_data()
    if request.method == 'POST':
        id = str(uuid.uuid4())
        name = request.form.get('name')
        price = int(request.form.get('price'))
        stock = int(request.form.get('stock'))

        temp_data = {
            'id': id,
            'name': name,
            'price': price,
            'stock': stock
        }

        json_data['dishes'].append(temp_data)
        print(json_data)
        save_data(json_data)
        print(
            f'id = {id} \n name = {name} \n price = ${price} \n stock = {stock}')
        # return 'Form has been submited'
    return render_template('home.html')


if __name__ == '__main__':
    os.environ['FLASK_ENV'] = 'development'
    os.environ['FLASK_DEBUG'] = '1'
    app.run(port=8000)
