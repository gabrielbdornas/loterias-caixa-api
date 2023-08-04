import urllib3
import requests
import pandas as pd

urllib3.disable_warnings()

BASE_URL = "https://servicebus2.caixa.gov.br/portaldeloterias/api/resultados/download"

jogos_list = [
    "+Milionária",
    "Mega-Sena",
    "Lotofácil",
    "Quina",
    "Lotomania",
    "Timemania",
    "Dupla-Sena",
    "Federal",
    "Loteca",
    "Dia-De-Sorte",
    "Super-Sete",
]


for jogo in jogos_list:
    res = requests.get(BASE_URL, params={"modalidade": jogo}, verify=False)

    if res.status_code == 200:
        with open(f'./data/excel/{jogo}.xlsx', 'wb') as file:
            file.write(res.content)
            
            df = pd.read_excel(f'./data/excel/{jogo}.xlsx', index_col=0)
            df.to_csv(f'./data/csv/{jogo}.csv')

            print(f'{jogo}.xlsx baixado.')
        continue

    raise Exception(f'Requisição falhou em {jogo}')