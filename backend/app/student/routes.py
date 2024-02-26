from app.extensions import db
from app.student import bp as app
from app.models import Student, Aule, MobileApp
from app.schemas import StudentSchema
from marshmallow import ValidationError
from flask_jwt_extended import jwt_required

from flask import jsonify, request

@jwt_required(locations=['cookies'])
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

@jwt_required(locations=['cookies'])
@app.route('/aules/<aule_id>/students', methods=['GET'])
def get_students_from_aule(mobile_app_id, aule_id):       
    aule = db.get_or_404(Aule, aule_id, description=f'Aule with id {aule_id} not found')
    schema = StudentSchema(many=True)
    
    return jsonify({'students': schema.dump(aule.students)}), 200
 
  
@app.route('/aules/<aule_code>/students', methods=['POST'])    
def post_student(mobile_app_id ,aule_code):
    db.get_or_404(MobileApp, mobile_app_id, description=f'App with id {mobile_app_id} not found')
    
    aule_code = aule_code.upper()
    aule = db.session.scalar(db.select(Aule).where(Aule.code == aule_code))
    if aule is None:
        return jsonify({'message': f'Aule with code {aule_code} not found'}), 404
    
    schema = StudentSchema()
    data = request.get_json()
    data['aule_id'] = aule.id
    
    print(data)
    try:
        validated_data = schema.load(data)
    except ValidationError as err:
        print(err.messages)
        return jsonify(err.messages), 422
    
    db.session.add(validated_data)
    db. session.commit()

    return jsonify({'student': schema.dump(validated_data)}), 201

    