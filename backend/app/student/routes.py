from app.extensions import db
from app.student import bp as app
from app.models.student import Student
from app.models.aule import Aule

from flask import jsonify, request


@app.route('', methods=['GET'])
def get_all_students():
    aule_id = request.args.get('aule_id')
    
    db.get_or_404(Aule, aule_id, description=f'Aule with id {aule_id} not found')

    students = (db.session.scalars(db.select(Student).where(Student.aule_id==aule_id)).all() 
                if aule_id 
                else db.session.scalars(db.select(Student)).all())

    return jsonify({'students': [student.serialize() for student in students]}), 200

    
@app.route('', methods=['POST'])    
def post_student():
    data = request.get_json()
    
    aule_id = data['aule_id']
    db.get_or_404(Aule, aule_id, description=f'Aule with id {aule_id} not found')
    
    student = create_student(data)
    if student is None:
        return jsonify({'message': 'missing data'}), 400
    
    return jsonify({'student': student.serialize()}), 201

def create_student(data):

    try:
        student = Student(data['first_name'], data['last_name'], data['last_name_2'], data['age'], data['aule_id'])
    except KeyError:
        return None
    
    if isinstance(student, Student):
        db.session.add(student)
        db.session.commit()
        return student

@app.route('/<int:id>', methods=['GET'])
def get_student(id):
    student = db.get_or_404(Student, id, description=f'Student with id {id} not found')
    
    return jsonify({'students': student.serialize()}), 200
    