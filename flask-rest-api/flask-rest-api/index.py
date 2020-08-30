from flask import Flask, jsonify

app = Flask(__name__)

students = [{"name": "Student 1"}, {"name": "Student 2"}]


@app.route("/students")
def get_students():
    return jsonify(students)
