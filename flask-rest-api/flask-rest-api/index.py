from flask import Flask, jsonify, request

app = Flask(__name__)

students = [{"id": 1, "name": "Student 1"}, {"id": 2, "name": "Student 2"}]


@app.route("/students/search")
def get_students():
    return jsonify(students)


@app.route("/students/info/<student_id>")
def get_student(student_id):
    result = None
    for student in students:
        if student["id"] == int(student_id):
            result = student
    result = {"error": "student not found!"} if result is None else result
    return jsonify(result)


@app.route("/students/create", methods=["POST"])
def create_student():
    students.append(request.get_json())
    return "", 204
