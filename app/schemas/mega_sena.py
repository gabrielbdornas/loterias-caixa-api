from app.ma import ma
from app.models import MegaSena


class MegaSenaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = MegaSena()
        load_instance = True
