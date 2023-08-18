from .base import Base
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import pandas as pd


class Base(DeclarativeBase):
    pass


class MegaSena(Base):
    __tablename__ = "mega_sena"

    concurso: Mapped[int] = mapped_column(primary_key=True)
    data_do_sorteio: Mapped[str] = mapped_column(nullable=True)
    bola1: Mapped[int] = mapped_column(nullable=True)
    bola2: Mapped[int] = mapped_column(nullable=True)
    bola3: Mapped[int] = mapped_column(nullable=True)
    bola4: Mapped[int] = mapped_column(nullable=True)
    bola5: Mapped[int] = mapped_column(nullable=True)
    bola6: Mapped[int] = mapped_column(nullable=True)
    ganhadores_6_acertos: Mapped[int] = mapped_column(nullable=True)
    cidade_uf: Mapped[str] = mapped_column(nullable=True)
    rateio_6_acertos: Mapped[str] = mapped_column(nullable=True)
    ganhadores_5_acertos: Mapped[int] = mapped_column(nullable=True)
    rateio_5_acertos: Mapped[str] = mapped_column(nullable=True)
    ganhadores_4_acertos: Mapped[int] = mapped_column(nullable=True)
    rateio_4_acertos: Mapped[str] = mapped_column(nullable=True)
    acumulado_6_acertos: Mapped[str] = mapped_column(nullable=True)
    arrecadacao_total: Mapped[str] = mapped_column(nullable=True)
    estimativa_premio: Mapped[str] = mapped_column(nullable=True)
    acumulado_sorteio_especial_mega_da_virada: Mapped[str] = mapped_column(
        nullable=True
    )
    observacao: Mapped[str] = mapped_column(nullable=True)


engine = create_engine("sqlite:///mydb.db", echo=True)
Base.metadata.create_all(engine)

with Session(engine) as session:
    df = pd.read_csv("../../data/csv/Mega-Sena.csv", index_col=0)
    # print(df)

    for index, row in df.iterrows():
        # print(f"index: {index}, row: {row}")
        # break
        data = MegaSena(
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
        session.add(data)

    session.commit()
