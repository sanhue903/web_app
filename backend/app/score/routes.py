from app.extensions import db
from app.student import bp as app
from app.models.student import Student
from app.models.aule import Aule
from app.models.mobile.score import Score
from app.models.mobile.question import Question
from app.models.mobile.chapter import Chapter
from backend.app.models.mobile.mobile_app import MobileApp

from flask import jsonify, request

@app.route('/students/<str:app_mobile_id>/scores', methods=['GET']) 
def get_all_scores_from_app(app_mobile_id):
    db.get_or_404(MobileApp, app_mobile_id, description=f'AppMobile with id {app_mobile_id} not found')
    
    scores = db.session.scalars(db.select(Score)).all()#cambiar query a solo los scores de la app
    
    return jsonify({
        'app_mobile': {
            'id': app_mobile_id,
            'scores': [score.serialize() for score in scores]
        }}), 200

@app.route('/students/<int:id>/scores', methods=['GET'])
def get_student_scores(id):
    student = db.get_or_404(Student, id, description=f'Student with id {id} not found')
    
    data = request.get_json()
    
    return jsonify({'students': student.serialize()}), 200
   
@app.route('/<int:id>/scores', methods=['POST'])
def post_student_scores(id):
    student = db.get_or_404(Student, id, description=f'Student with id {id} not found')
    
    return jsonify({'students': student.serialize()}), 200

score = {
    'student_id': '1',
    'app_mobile': {
        'id': 'BOTIQI',
        'chapter': {
            'id': 'CONEMO',
            'questions': {{
                    'id': 'TRISTE',
                    'score':{
                        'time': '100',
                        'attemps': 2
                    }
                },
                {
                    'id': 'FELIZZ',
                    'score':{
                        'time': '100',
                        'attemps': 2
                    }
                }
            }
        }
    }
}