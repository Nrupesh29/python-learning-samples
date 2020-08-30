from flask import Flask

app = Flask(__name__)

students = [{"name": "Student 1"}, {"name": "Student 2"}]


@app.route("/")
def main():
    return "Hello, World!"
