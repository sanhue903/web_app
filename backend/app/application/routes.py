from app.application import bp as app
from app.extensions import db
from app.models import Application
from flask_jwt_extended import create_access_token, jwt_required

from flask import jsonify, request

@app.route('/register', methods=['POST'])
@jwt_required(locations=['headers'])
def app_aplication():
    data = request.get_json()
    
    app = Application(data['id'], data['name'])
    db.session.add(app)
    db.session.commit()
    access_token = create_access_token(identity=app.id, expires_delta=False)
    
    response = jsonify({'token': access_token}), 201
    return response

@app.route('/<app_id>', methods=['GET'])
@jwt_required(locations=['headers'])
def get_application(app_id):
    app = db.session.scalar(db.select(Application).where(Application.id == app_id))
    
    if app is None:
        return jsonify({'message': f'Application with id {app_id} not found'}), 404
    
    access_token = create_access_token(identity=app.id, expires_delta=False)
    
    return jsonify({'token': access_token}), 200