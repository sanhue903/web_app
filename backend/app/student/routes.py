from app.extensions import db
from app.student import bp as app
from app.models.student import Student
from app.models.aule import Aule
from app.models.mobile.score import Score
from app.models.mobile.question import Question
from app.models.mobile.chapter import Chapter
from backend.app.models.mobile.mobile_app import MobileApp
from app.schemas.student_schema import StudentSchema

from flask import jsonify, request

@app.route('', methods=['GET'])
def get_all_students():
    aule_id = request.args.get('aule_id')
    
    if aule_id:    
        db.get_or_404(Aule, aule_id, description=f'Aule with id {aule_id} not found')

    students = (db.session.scalars(db.select(Student).where(Student.aule_id==aule_id)).all() 
                if aule_id 
                else db.session.scalars(db.select(Student)).all())

    return jsonify({'students': [student.serialize() for student in students]}), 200

    
@app.route('', methods=['POST'])    
def post_student():
   # schema = StudentSchema()
    #validated_data = schema.load(request.get_json())
    #schema.
    
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

@app.route('/<int:user_id>', methods=['GET'])
def get_student(user_id):
    student = db.get_or_404(Student, user_id, description=f'Student with id {user_id} not found')
    
    return jsonify({'students': student.serialize()}), 200

