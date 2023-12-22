from app.auth import bp as app
from app.extensions import db
from app.models import User
from app.schemas import LoginSchema, SignUpSchema
from marshmallow import ValidationError
from flask_jwt_extended import create_access_token, set_access_cookies

from flask import jsonify, request


@app.route('/login', methods=['GET'])
def login_web():
    data = request.get_json()
    schema = LoginSchema()
    
    try:
        validated_data = schema.load(data)
    except ValidationError as err:
        return jsonify(err.messages), 422
    
    user = db.session.scalar(db.select(User).where(User.username == validated_data['username']))
   
    if not user.check_password(validated_data['password']):
        return jsonify({'message': 'Wrong password'}), 401
    
    access_token = create_access_token(identity=user.id)
    
    response = jsonify({'message': 'login successful'}), 200
    set_access_cookies(response, access_token)
    
    return response 

@app.route('/api/login', methods=['GET'])
def login_api():
    data = request.get_json()
    schema = LoginSchema()
    
    try:
        validated_data = schema.load(data)
    except ValidationError as err:
        return jsonify(err.messages), 422
    
    user = db.session.scalar(db.select(User).where(User.username == validated_data['username']))
   
    if not user.check_password(validated_data['password']):
        return jsonify({'message': 'Wrong password'}), 401
    
    access_token = create_access_token(identity=user.id)
    
    response = jsonify({'token': access_token}), 200

    
    return response 

@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    
    schema = SignUpSchema()
    try:
        validated_data = schema.load(data)
    except ValidationError as err:
        return jsonify(err.messages), 422

    if db.session.scalar(db.select(User).where(User.username == validated_data['username'])) is not None:
        return jsonify({'message': 'User already exists'}), 409
    
    if db.session.scalar(db.select(User).where(User.username == validated_data['username'])) is not None:
        return jsonify({'message': 'this email adress has already been registered'}), 409
    
    
    if data['password'] != validated_data['confirm_password']:
        return jsonify({'message': 'Passwords do not match'}), 400
    
    validated_data.pop('confirm_password')
    user = create_user(validated_data)
    
    
    
    return jsonify({'message': f'User {user.username} created'}), 201


def create_user(data):
    new_user = User(**data)
    db.session.add(new_user)
    db.session.commit()
    
    return new_user