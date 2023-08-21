from flask import Blueprint
from app.models import mega_sena as model
from flask import jsonify
from app.schemas import mega_sena as schema

api_bp = Blueprint("api", __name__)


@api_bp.get("/healthz")
def health_check():
    """
    Exemplo de rota de api.
    """
    return {"status": "online"}


@api_bp.get("/mega-senas")
def get_mega_sena():
    mega_sena = model.MegaSena()
    mega_senas = mega_sena.query.all()
    schemas = schema.MegaSenaSchema(many=True)
    return jsonify(schemas.dump(mega_senas)), 200
