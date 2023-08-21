from flask import Flask
from flask_migrate import Migrate
from app.models.mega_sena import MegaSena

from app.config import config
from app.cli import seed_cli
from app.db import db
from app.routes import api_bp

migrate = Migrate()


def create_app() -> Flask:
    """
    Cria a aplicação principal.

    TODO: Passar configuração da aplicação como argumento da função para facilitar testes.

    Rodar no terminal:
    `flask db migrate` cria os arquivos na pasta migrations com a estrutura das models (pega criações ou alterações de models e gera os arquivos para poder aplicar).

    `flask db upgrade` para aplicar os scripts na pasta migrations.
    """

    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app=app)
    migrate.init_app(app=app, db=db)

    app.register_blueprint(api_bp, url_prefix="/api/v1")

    app.cli.add_command(seed_cli)

    return app
