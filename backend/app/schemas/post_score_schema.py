from app.extensions import ma
from marshmallow import fields, validate


class InnerScoreSchema(ma.Schema):
    seconds = fields.Float(required=True)
    is_correct = fields.Boolean(required=True)
    answer = fields.Str(required=True)
    question_id = fields.Str(required=True, validate=validate.Length(min=6, max=6))

class ChapterSchema(ma.Schema):
    id = fields.Str(required=True, validate=validate.Range(min=6, max=6))
    scores = fields.List(fields.Nested(InnerScoreSchema), required=True)

class AppMobileSchema(ma.Schema):
    id = fields.Str(required=True, validate=validate.Range(min=6, max=6))
    chapter = fields.Nested(ChapterSchema, required=True)

class PostScoreSchema(ma.Schema):
    student_id = fields.Str(required=True)
    app_mobile = fields.Nested(AppMobileSchema, required=True)
    
    