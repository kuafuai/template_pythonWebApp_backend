from flask import Blueprint, jsonify

from app.models import Student

routes = Blueprint('routes', __name__)

students = [
    Student('001', 'Alice', 'Female', '1990-01-01', 'Class A', 'Computer Science'),
    Student('002', 'Bob', 'Male', '1991-02-02', 'Class B', 'Mathematics'),
    Student('003', 'Charlie', 'Male', '1992-03-03', 'Class C', 'Physics'),
]

@routes.route('/students', methods=['GET'])
def get_students():
    return jsonify([student.__dict__ for student in students])

@routes.route('/students/<student_id>', methods=['GET'])
def get_student(student_id):
    student = next((student for student in students if student.student_id == student_id), None)
    if student:
        return jsonify(student.__dict__)
    else:
        return jsonify({'error': 'Student not found'})

@routes.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()
    student = Student(data['student_id'], data['name'], data['gender'], data['birthdate'], data['class'], data['college'])
    students.append(student)
    return jsonify({'message': 'Student added successfully'})

@routes.route('/students/<student_id>', methods=['PUT'])
def update_student(student_id):
    data = request.get_json()
    student = next((student for student in students if student.student_id == student_id), None)
    if student:
        student.name = data['name']
        student.gender = data['gender']
        student.birthdate = data['birthdate']
        student.class = data['class']
        student.college = data['college']
        return jsonify({'message': 'Student updated successfully'})
    else:
        return jsonify({'error': 'Student not found'})

@routes.route('/students/<student_id>', methods=['DELETE'])
def delete_student(student_id):
    student = next((student for student in students if student.student_id == student_id), None)
    if student:
        students.remove(student)
        return jsonify({'message': 'Student deleted successfully'})
    else:
        return jsonify({'error': 'Student not found'})
