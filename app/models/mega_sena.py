from .base import Base
from sqlalchemy.orm import Mapped,mapped_column

class MegaSena(Base):
    __tablename__ = "mega_sena"
    concurso:Mapped[int] = mapped_column(unique=True)
    data_do_sorteio:Mapped[str]
    bola1:Mapped[int]
    bola2:Mapped[int]
    bola3:Mapped[int]
    bola4:Mapped[int]
    bola5:Mapped[int]
    bola6:Mapped[int]
    ganhadores_6_acertos:Mapped[int]
    cidade_uf:Mapped[str]
    rateio_6_acertos:Mapped[str]
    ganhadores_5_acertos:Mapped[int]
    rateio_5_acertos:Mapped[str]
    ganhadores_4_acertos:Mapped[int]
    rateio_4_acertos:Mapped[str]
    acumulado_6_acertos:Mapped[str]
    arrecadao_total:Mapped[str]
    estimativa_premio:Mapped[str]
    acumulado_sorteio_especial_mega_da_virada:Mapped[str]
    observacao:Mapped[str]

