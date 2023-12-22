from app.aules import bp as app
from app.extensions import db
from app.models import Aule
from app.schemas import AuleSchema
from flask_jwt_extended import jwt_required

from flask import request, jsonify

@jwt_required(locations=['cookies'])
@app.route('', methods=['GET'])
def get_aules(mobile_app_id):
    aules = db.session.scalars(db.select(Aule).where(Aule.mobile_app_id == mobile_app_id)).all()
    
    schema = AuleSchema(many=True)
    return jsonify({'aules': schema.dump(aules)}), 200
    
@jwt_required(locations=['cookies'])
@app.route('', methods=['POST'])
def post_aule(mobile_app_id):
    data = request.get_json()
    schema = AuleSchema()
    
    validated_data = schema.load(data)
    
    aule = create_aule(mobile_app_id, validated_data)
    
    return schema.jsonify({'aule': schema.dump(aule)}), 201
    
@jwt_required(locations=['cookies'])
@app.route('/<aule_id>', methods=['GET'])
def get_aule(aule_id, mobile_app_id):
    schema = AuleSchema()
    aule = db.get_or_404(Aule, aule_id, description=f'Aule with id {aule_id} not found')
    
    return schema.jsonify({'aule': schema.dump(aule)}), 200

def create_aule(mobile_app_id, data):
    aule = Aule(
        mobile_app_id=mobile_app_id,
        **data
    )
    db.session.add(aule)
    db.session.commit()
    return aule   
    
@jwt_required(locations=['cookies'])
@app.route('/<aule_id>', methods=['PUT'])       
def open_aule(aule_id):
    aule = db.get_or_404(Aule, aule_id, description=f'Aule with id {aule_id} not found')
    aule.generate_temporal_code()
    db.session.commit()
    
    aule.schedule_reset_code()
    
    return jsonify({'code': aule.code}), 201