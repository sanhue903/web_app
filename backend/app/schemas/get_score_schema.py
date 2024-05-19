from app.extensions import ma
from marshmallow import fields, validate

class InnerScoreSchema(ma.Schema):
    student_id = fields.Integer(required=True)
    seconds = fields.Float(required=True)
    is_correct = fields.Boolean(required=True)
    answer = fields.String(required=True)

class QuestionSchema(ma.Schema):
    id = fields.Str(required=True, validate=validate.Length(equal=6))
    score = fields.List(fields.Nested(InnerScoreSchema))

class GetScoreSchema(ma.Schema):
    id = fields.Str(required=True, validate=validate.Length(equal=6))
    question = fields.List(fields.Nested(QuestionSchema))
    load_instance = True