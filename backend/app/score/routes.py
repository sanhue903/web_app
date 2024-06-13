from app.extensions import db
from app.score import bp as app
from app.models import Student, Score, Application, Chapter, Question, User
from app.schemas import PostScoreSchema, GetScoreSchema
from marshmallow import ValidationError
from flask_jwt_extended import jwt_required, get_jwt_identity

from flask import jsonify, request

def get_scores_from_student():
    pass

@app.route('/scores', methods=['GET'])
@jwt_required(locations=['headers'])
def get_scores_from_students(app_id):
    app = db.session.scalar(db.select(Application).where(Application.id == app_id))
    if app is None:
        return jsonify({'message': f'App with id {app_id} not found'}), 404
    
    user_id = get_jwt_identity()    
    user = db.session.scalar(db.select(User).where(User.id == user_id))
    if user is None:
        return jsonify({'message': 'Unauthorized'}), 401
    
    #pagination
    page = request.args.get('page', 1, type=int) 
    limit = request.args.get('limit', 20, type=int)

    #filters
    chapter = request.args.get('chapter', None, type=str)
    question = request.args.get('question', None, type=str)
    attempt = request.args.get('attempts', 1, type=int)
    
    scores = db.paginate(db.select(Score).where(Score.student_id == Student.id).where(Student.app_id == app_id).where(Score.attempts == attempt), page=page, per_page=limit, max_per_page=100).items
    
    return jsonify({'message': 'Not implemented'}), 501
    
    
    
    
    
    
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
    
@app.route('/scores', methods=['POST'])
@jwt_required(locations=['headers'])
def post_student_scores():
    json_data = request.get_json()
    schema = PostScoreSchema()
    try:
        validated_data = schema.load(json_data)
    except ValidationError as err:
        return jsonify(err.messages), 422
    
    student = db.session.scalar(db.select(Student).where(Student.id == validated_data['student_id']))
    db.get_or_404(Application, validated_data['app_mobile']['id'], description=f'AppMobile with id {validated_data["app_mobile"]["id"]} not found')
    db.get_or_404(Chapter, validated_data['app_mobile']['chapter']['id'], description=f'Chapter with id {validated_data["app_mobile"]["chapter"]["id"]} not found')
    
    
    for question in validated_data['app_mobile']['chapter']['questions']:
        db.get_or_404(Question, question['id'], description=f'Question with id {question["id"]} not found')
        
        score = Score(student.id, question['id'], seconds=question['score']['time'], is_correct=question['score']['is_correct'], answer=question['score']['answer'])
        db.session.add(score)
        db.session.commit()
    
    return jsonify({'message': 'scores added correcly'}), 201