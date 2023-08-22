from flask import Blueprint, jsonify

from app.models import MegaSena
from app.schemas import MegaSenaSchema

api_bp = Blueprint("api", __name__)


@api_bp.get("/healthz")
def health_check():
    """
    Exemplo de rota de api.
    """
    return {"status": "online"}


@api_bp.get("/mega-senas")
def get_mega_sena():
    mega_senas = MegaSena.find_all()
    schema = MegaSenaSchema(many=True)
    return jsonify(schema.dump(mega_senas))


@api_bp.get("/mega-senas/<int:id>")
def get_mega_sena_teste(id: int):
    mega_sena = MegaSena.find_by_id(id)

    if mega_sena is None:
        return {"message": "Jogo não encontrado"}, 404

    schema = MegaSenaSchema()
    return jsonify(schema.dump(mega_sena))
