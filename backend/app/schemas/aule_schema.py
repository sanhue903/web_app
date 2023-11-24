from app.extensions import ma
from app.models import Aule

class AuleSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Aule 
        load_instance = True
        exclude = ['mobile_app_id', 'students']