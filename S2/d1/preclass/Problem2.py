from flask import Flask, request, render_template,jsonify
import os
import json

if __name__ == '__main__':
    os.environ['FLASK_ENV'] = 'development'
    os.environ['FLASK_DEBUG'] = '1'


app = Flask(__name__)


def load_data():
    with open("data.json", 'r') as f:
        data = json.load(f)
    return data

def save_data(json_data):
    with open("data.json", 'w') as f:
        json.dump(json_data,f)


@app.route("/")
def Home():
    return "Home Page CRUD."


@app.route("/create", methods=["GET", "POST"])
def create():
    json_data = load_data()

    if request.method == 'POST':
        name = request.form.get("name")
        email = request.form.get("email")
        print(f'{name} {email}')
        entry_data = {'name': name, 'email': email}
        json_data.append(entry_data)
    

        with open('data.json', 'w') as f:
            json.dump(json_data, f)
        return f"Congratulations Form has been submitted"

    return render_template('form.html')


@app.route("/read")
def read():
    data = jsonify(load_data())
    return data

@app.route('/update/<int:index>', methods=['GET', 'POST'])
def update(index):
    json_data = load_data()
    print(index)
    if index < len(json_data):
        if request.method == 'POST':
            name = request.form.get('name')
            email = request.form.get('email')
            print(f'name {name}\n email {email}')

            json_data[index]['name'] = name
            json_data[index]['email'] = email

            save_data(json_data)
            print(json_data)
            return 'Entry updated successfully.'
        else:
            existing_entry = json_data[index]
            print(existing_entry)
            return render_template('form.html', entry=existing_entry)
    else:
        return 'Invalid index.'



@app.route('/delete/<int:index>', methods=['DELETE'])
def delete(index):
    print("index", index)
    data = load_data()

    # Delete entry at specified index
    if index < len(data):
        del data[index]
        save_data(data)
        return 'Entry deleted successfully.'
    else:
        return 'Invalid index.'


if __name__ == '__main__':
    app.run(port=8000)
