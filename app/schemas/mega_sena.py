from app.schemas import ma
from app.models import MegaSena


class MegaSenaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = mega_sena.MegaSena()
        load_instance = True
