from app.extensions import db
from app.student import bp as app
from app.models import Student, Application, User
from app.schemas import StudentSchema
from marshmallow import ValidationError
from flask_jwt_extended import jwt_required, get_jwt_identity

from flask import jsonify, request

@app.route('',methods=['GET'])
@jwt_required(locations=['headers'])
def get_students_from_app(app_id):
    app = db.session.scalar(db.select(Application).where(Application.id == app_id))
    if app is None:
        return jsonify({'message': f'App with id {app_id} not found'}), 404
    
    user_id = get_jwt_identity()
    user = db.session.scalar(db.select(User).where(User.id == user_id))
    if user is None:
        return jsonify({'message': 'Unauthorized'}), 401
    
    page = request.args.get('page', 1, type=int)
    limit = request.args.get('limit', 20, type=int)

    students = db.paginate(db.select(Student).where(Student.app_id == app_id), page=page, per_page=limit,max_per_page=100).items
    
    schema = StudentSchema(many=True)

    return jsonify({'students': schema.dump(students)}), 200
#TODO cambiar
#@jwt_required(locations=['cookies'])
#@app.route('/<aule_id>/students', methods=['GET'])
#def get_students_from_aule(mobile_app_id, aule_id):       
#    aule = db.get_or_404(Aule, aule_id, description=f'Aule with id {aule_id} not found')
#    schema = StudentSchema(many=True)
    
#    return jsonify({'students': schema.dump(aule.students)}), 200
 
  
@app.route('',methods=['POST'])    
@jwt_required(locations=['headers'])
def post_student(app_id):
    app = db.session.scalar(db.select(Application).where(Application.id == app_id))
    if app is None:
        return jsonify({'message': f'App with id {app_id} not found'}), 404
    
    if get_jwt_identity() != app_id:
        return jsonify({'message': 'Unauthorized'}), 401
    
    schema = StudentSchema()

    data = request.get_json()
    data['app_id'] = app_id
    
    try:
        validated_data: Student = schema.load(data)
    except ValidationError as err:
        print(err.messages)
        return jsonify(err.messages), 422
    
    db.session.add(validated_data)
    db. session.commit()

    return jsonify({'student': schema.dump(validated_data)}), 201