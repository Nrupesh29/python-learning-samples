from flask import Flask, jsonify

app = Flask(__name__)

students = [{"id": 1, "name": "Student 1"}, {"id": 2, "name": "Student 2"}]


@app.route("/students/search")
def get_students():
    return jsonify(students)


@app.route("/students/info/<student_id>")
def get_student(student_id):
    return jsonify(
        next(student for student in students if student["id"] == int(student_id))
    )
