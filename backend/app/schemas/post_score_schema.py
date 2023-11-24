from app.extensions import ma
from marshmallow import fields, validate


class InnerScoreSchema(ma.Schema):
    miliseconds = fields.Int(required=True)
    attempts = fields.Int(required=True)

class QuestionSchema(ma.Schema):
    id = fields.Str(required=True, validate=validate.Length(min=6, max=6))
    score = fields.Nested(InnerScoreSchema, required=True)

class ChapterSchema(ma.Schema):
    id = fields.Str(required=True, validate=validate.Range(min=6, max=6))
    questions = fields.List(fields.Nested(QuestionSchema), required=True)

class AppMobileSchema(ma.Schema):
    id = fields.Str(required=True, validate=validate.Range(min=6, max=6))
    chapter = fields.Nested(ChapterSchema, required=True)

class PostScoreSchema(ma.Schema):
    student_id = fields.Str(required=True)
    app_mobile = fields.Nested(AppMobileSchema, required=True)
    
    