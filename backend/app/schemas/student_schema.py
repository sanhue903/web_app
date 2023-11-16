from app.extensions import ma
from app.models.student import Student

class StudentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Student    
    