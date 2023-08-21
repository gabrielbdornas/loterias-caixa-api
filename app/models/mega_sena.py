from .base import Base
from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column
from pandas import Series


class MegaSena(Base):
    __tablename__ = "mega_sena"

    concurso: Mapped[int] = mapped_column(unique=True)
    data_do_sorteio: Mapped[Optional[str]]  # fazer o parse dessa data
    bola1: Mapped[Optional[int]]
    bola2: Mapped[Optional[int]]
    bola3: Mapped[Optional[int]]
    bola4: Mapped[Optional[int]]
    bola5: Mapped[Optional[int]]
    bola6: Mapped[Optional[int]]
    ganhadores_6_acertos: Mapped[Optional[int]]
    cidade_uf: Mapped[Optional[str]]
    rateio_6_acertos: Mapped[Optional[str]]
    ganhadores_5_acertos: Mapped[Optional[int]]
    rateio_5_acertos: Mapped[Optional[str]]
    ganhadores_4_acertos: Mapped[Optional[int]]
    rateio_4_acertos: Mapped[Optional[str]]
    acumulado_6_acertos: Mapped[Optional[str]]
    arrecadacao_total: Mapped[Optional[str]]
    estimativa_premio: Mapped[Optional[str]]
    acumulado_sorteio_especial_mega_da_virada: Mapped[Optional[str]]
    observacao: Mapped[Optional[str]]

    # Retorna instância da própria classe para salvar no banco
    @classmethod
    def from_csv(cls, index: int, row: Series):
        return cls(
            concurso=index,
            data_do_sorteio=row["Data do Sorteio"],
            bola1=row["Bola1"],
            bola2=row["Bola2"],
            bola3=row["Bola3"],
            bola4=row["Bola4"],
            bola5=row["Bola5"],
            bola6=row["Bola6"],
            ganhadores_6_acertos=row["Ganhadores 6 acertos"],
            cidade_uf=row["Cidade / UF"],
            rateio_6_acertos=row["Rateio 6 acertos"],
            ganhadores_5_acertos=row["Ganhadores 5 acertos"],
            rateio_5_acertos=row["Rateio 5 acertos"],
            ganhadores_4_acertos=row["Ganhadores 4 acertos"],
            rateio_4_acertos=row["Rateio 4 acertos"],
            acumulado_6_acertos=row["Acumulado 6 acertos"],
            arrecadacao_total=row["Arrecadação Total"],
            estimativa_premio=row["Estimativa prêmio"],
            acumulado_sorteio_especial_mega_da_virada=row[
                "Acumulado Sorteio Especial Mega da Virada"
            ],
            observacao=row["Observação"],
        )
