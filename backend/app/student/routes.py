from app.extensions import db
from app.student import bp as app
from app.models import Student, Aule, MobileApp
from app.schemas import StudentSchema
from marshmallow import ValidationError


from flask import jsonify, request

@app.route('/students', methods=['GET'])
def get_students_from_mobile_app(mobile_app_id):
    db.get_or_404(MobileApp, mobile_app_id, description=f'App with id {mobile_app_id} not found')
    schema = StudentSchema(many=True)
    aules = db.session.scalars(db.select(Aule).where(Aule.mobile_app_id==mobile_app_id)).all()
    students = []
    
    for aule in aules:
        aule_students = db.session.scalars(db.select(Student).where(Student.aule_id==aule.id)).all()
        students+= aule_students

    return jsonify({'students': schema.dump(students)}), 200

@app.route('/aules/<aule_id>/students', methods=['GET'])
def get_students_from_aule(mobile_app_id, aule_id):       
    aule = db.get_or_404(Aule, (aule_id, mobile_app_id), description=f'App with id {mobile_app_id} or Aule with id {aule_id} not found')
    schema = StudentSchema(many=True)
    
    return jsonify({'students': schema.dump(aule.students)}), 200
    
@app.route('/aules/<aule_id>/students', methods=['POST'])    
def post_student(mobile_app_id, aule_id):
    db.get_or_404(Aule, (aule_id, mobile_app_id), description=f'App with id {mobile_app_id} or Aule with id {aule_id} not found')
    
    schema = StudentSchema()
    try:
        validated_data = schema.load(request.get_json())
    except ValidationError as err:
        return jsonify(err.messages), 422
    
    student = create_student(validated_data)

    return jsonify({'student': schema.dump(student)}), 201

def create_student(data):
    new_student = Student(**data)
    db.session.add(new_student)
    db. session.commit()
    
    return new_student
    