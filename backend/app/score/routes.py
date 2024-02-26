from app.extensions import db
from app.score import bp as app
from app.models import Student, Score, MobileApp, Chapter, Question, Aule
from app.schemas import PostScoreSchema, GetScoreSchema
from marshmallow import ValidationError
from flask_jwt_extended import jwt_required

from flask import jsonify, request

@jwt_required(locations=['cookies'])
@app.route('/students/scores', methods=['GET'])
def get_student_scores_from_aule(aule_code):
    aule_code = aule_code.upper()
    aule = db.session.scalar(db.select(Aule).where(Aule.code == aule_code))
    
    if aule is None:
        return jsonify({'message': f'Aule with code {aule_code} not found'}), 404
    
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
            scores = db.session.scalars(db.select(Score).where(Score.question_id == question.id).where(Score.student_id == Student.id).where(Student.aule_code == aule.code)).all()
            for score in scores:
                score_data = {
                    'student_id': score.student_id,
                    'miliseconds': score.miliseconds,
                    'attempts': score.attempts
                }
                question_data['score'].append(score_data)
            chapter_data['chapter']['question'].append(question_data)
        results.append(chapter_data)
        
        
    print(results)
    return jsonify({'results': results}), 200
    #TODO fix schema
    schema = GetScoreSchema()
    try:
        data = schema.load(results)
    except ValidationError as err:
        return jsonify(err.messages), 422
        
    return jsonify({'results': data}), 200
    
@jwt_required(locations=['headers'])
@app.route('/students/scores', methods=['POST'])
def post_student_scores(aule_code):
    aule_code = aule_code.upper()
    aule = db.session.scalar(db.select(Aule).where(Aule.code == aule_code))
    
    if aule is None:
        return jsonify({'message': f'Aule with code {aule_code} not found'}), 404
    
    json_data = request.get_json()
    schema = PostScoreSchema()
    try:
        validated_data = schema.load(json_data)
    except ValidationError as err:
        return jsonify(err.messages), 422
    
    student = db.session.scalar(db.select(Student).where(Student.aule_id == aule.id).where(Student.id == validated_data['student_id']))
    db.get_or_404(MobileApp, validated_data['app_mobile']['id'], description=f'AppMobile with id {validated_data["app_mobile"]["id"]} not found')
    db.get_or_404(Chapter, validated_data['app_mobile']['chapter']['id'], description=f'Chapter with id {validated_data["app_mobile"]["chapter"]["id"]} not found')
    
    
    for question in validated_data['app_mobile']['chapter']['questions']:
        db.get_or_404(Question, question['id'], description=f'Question with id {question["id"]} not found')
        
        score = Score(student.id, question['id'], miliseconds=question['score']['time'], attempts=question['score']['attemps'])
        db.session.add(score)
        db.session.commit()
    
    return jsonify({'message': 'scores added correcly'}), 201
