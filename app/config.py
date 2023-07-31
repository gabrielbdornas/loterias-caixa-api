from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    """
    Carrega e valida as configurações básicas da aplicação do arquivo `.env`
    na raiz do projeto usando pydantic-settings.

    A validação das variáveis de ambiente é feita com base no tipo anotado.

    [Referência](https://docs.pydantic.dev/latest/usage/pydantic_settings/)
    """

    model_config = SettingsConfigDict(env_file=".env")

    DEBUG: bool = True
    SECRET_KEY: str
    SQLALCHEMY_DATABASE_URI: str


config = Config()
