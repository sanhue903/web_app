from app.extensions import db
from app.score import bp as app
from app.models import Student, Score, MobileApp, Chapter, Question, Aule
from app.schemas import ScoreSchema
from marshmallow import ValidationError

from flask import jsonify, request

@app.route('/students/scores', methods=['GET'])
def get_student_scores(mobile_app_id, aule_id):
    aule = db.get_or_404(Aule, (aule_id, mobile_app_id), description=f'App with id {mobile_app_id} or Aule with id {aule_id} not found')

    results = []
    for chapter in aule.mobile_app.chapters:
        chapter_data = {
            'chapter': {
                'id': chapter.id,
                'question': []
            }
        }
        for question in chapter.questions:
            question_data = {
                'id': question.id,
                'score': []
            }
            scores = db.session.scalars(db.select(Score).where(Score.question_id == question.id).where(Score.student_id == Student.id).where(Student.mobile_app_id == mobile_app_id).where(Student.aule_id == aule.id)).all()
            for score in scores:
                score_data = {
                    'student_id': score.student_id,
                    'time': score.time,
                    'attempts': score.attempts
                }
                question_data['score'].append(score_data)
            chapter_data['chapter']['question'].append(question_data)
        results.append(chapter_data)
        
    return jsonify({'results': results}), 200
    

@app.route('/students/scores', methods=['POST'])
def post_student_scores():
    
    json_data = request.get_json()
    schema = ScoreSchema()
    try:
        data = schema.load(json_data)
    except ValidationError as err:
        return jsonify(err.messages), 422
    
    student_id = db.get_or_404(Student, data['student_id'], description=f'Student with id {data["student_id"]} not found')
    db.get_or_404(MobileApp, data['app_mobile']['id'], description=f'AppMobile with id {data["app_mobile"]["id"]} not found')
    db.get_or_404(Chapter, data['app_mobile']['chapter']['id'], description=f'Chapter with id {data["app_mobile"]["chapter"]["id"]} not found')
    
    
    for question in data['app_mobile']['chapter']['questions']:
        db.get_or_404(Question, question['id'], description=f'Question with id {question["id"]} not found')
        
        score = Score(student_id, question['id'], miliseconds=question['score']['time'], attempts=question['score']['attemps'])
        db.session.add(score)
        db.session.commit()
    
    return jsonify({'message': 'scores added correcly'}), 201
