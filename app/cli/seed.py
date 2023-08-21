import click
import pandas as pd
from flask.cli import AppGroup
from app.models import MegaSena

MEGA_SENA_PATH = "data/csv/Mega-Sena.csv"

seed_cli = AppGroup("seed")


@seed_cli.command("mega-sena")
@click.option("--file_path", default=MEGA_SENA_PATH)
def seed_mega_sena():
    # print("Ler e inserir dados mega sena")
    df = pd.read_csv(MEGA_SENA_PATH, index_col=0)
    # print(df)

    for index, row in df.iterrows():
        # print(f"index: {index}, row: {row}")
        # break
        data = MegaSena.from_csv(index, row)
        data.save()


@seed_cli.command("download-games")
def download_games():
    print("baixar arquivos aqui")
