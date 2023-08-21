from sqlalchemy import select
from sqlalchemy.orm import Mapped, mapped_column
from app.db import db


class Base(db.Model):
    """
    Representa uma entidade base do banco de dados. Deve ser herdada pelas demais models
    para evitar repetição desnecessária de código.

    Exemplo:
    ```python
    from typing import Optional

    from sqlalchemy.orm import Mapped, mapped_column

    from .base import Base

    class User(Base):
        name: Mapped[Optional[str]]
        email: Mapped[str] = mapped_column(unique=True)
        password_hash: Mapped[str]
        # ... demais campos e métodos
    ```

    O pacote flask_sqlalchemy é apenas um `wrapper` do pacote sqlalchemy, então as models
    podem ser definidas usando imports diretamente do sqlalchemy.

    A nova versão do sqlalchemy altera a maneira recomendada de declarar models utilizando
    anotação de tipos com `Mapped` e definindo atributos das colunas usando `mapped_column`.

    [Referência ORM](https://docs.sqlalchemy.org/en/20/orm/quickstart.html)

    `__abstract__ = True` diz pro SQLAlchemy que a classe Base não representa uma tabela do banco e que suas propriedades e métodos devem ser herdados.

    [Referência] https://stackoverflow.com/questions/22976445/how-do-i-declare-a-base-model-class-in-flask-sqlalchemy
    """

    __abstract__ = True
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    @classmethod
    def find_by_id(cls, id: int):
        """
        Busca um objeto com base no `id`.
        """
        stmt = select(cls).where(cls.id == id)
        return db.session.execute(stmt).scalar()

    def save(self):
        """
        Insere ou atualiza um objeto no banco de dados.
        """
        db.session.add(self)
        db.session.commit()
        db.session.refresh(self)

    def delete(self):
        """
        Apaga uma entidade do banco de dados.
        """
        db.session.delete(self)
        db.session.commit()
