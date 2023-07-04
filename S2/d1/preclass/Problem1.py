from flask import Flask

app = Flask(__name__)


@app.route("/")
def Home():
    return "Home Page"


@app.route("/greet/<username>")
def greet(username):
    return f"Congratulations {username} Sir ji"


@app.route("/farewell/<username>")
def farewell(username):
    return f'farewell {username} sir ji'


if __name__ == '__main__':
    app.run(port=8000)
