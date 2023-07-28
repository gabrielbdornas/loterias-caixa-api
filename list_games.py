import urllib3
import requests

urllib3.disable_warnings()

BASE_URL = "https://servicebus2.caixa.gov.br/portaldeloterias/api/resultados/download"

jogos_list = [
    "Teste",
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
        with open(f"./jogos/{jogo}.xlsx", "wb") as file:
            file.write(res.content)
            print(f"{jogo}.xlsx baixado.")
        continue

    raise Exception("Requisição falhou")


# verify = False: erro de certificação no https da página. Usa verify para não fazer verificação de certificado e ignorar o erro.
# requisition status code == 200: significa que deu tudo certo na requisição
# with: usado para file handling. Permite que o arquivo seja fechado automaticamente assim que as operações dentro do with sejam realizadas.
# open f: f string, para passar a variável
# wb: write bytes. A requisição é recebida em bytes. Dessa forma, deve escrever no arquivo a ser criado em bytes (passar o mouse em write e content para conferir, com pylance instalado)
# continue: mantém o loop rodando enquanto as requisições dão certo
# raise Exception: apresenta mensagem de erro e interrompe o loop quando a requisição não dá certo.
# levantamento de erros, pensar como melhorar:
# 1. Ver se a tarefa tem que ser feita 100% (raise exception para interromper o loop).
# 2. Caso não tenha, pensar outra forma (continua o loop e gera o restante dos arquivos, por exemplo).
# 3. Servidor deve sempre estar rodando.
# 4. Aprofundar estudos sobre isso: ler docs de try-except, raise Exception, error_handler (flask)
