from flask import Flask, jsonify, request

app = Flask(__name__)

students = [
    {"name": "Student 1", "age": 17},
    {"name": "Student 2", "age": 23},
]


@app.route("/students/")
def get_students():
    return jsonify(students), 200


@app.route("/students/<int:student_id>/", methods=["PUT"])
def update_student(student_id):
    students[student_id] = request.get_json()
    return jsonify(students[student_id]), 200


@app.route("/students/", methods=["POST"])
def create_student():
    students.append(request.get_json())
    return "", 200


@app.route("/students/<int:student_id>/", methods=["DELETE"])
def delete_student(student_id):
    students.pop(student_id)
    return "None", 200


app.run()
