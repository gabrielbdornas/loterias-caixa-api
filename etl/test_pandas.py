from frictionless import Package
import pandas as pd

df = pd.read_excel("../data/excel/Mega-Sena.xlsx", index_col=0)
df.to_csv("../data/csv/Mega-Sena.csv")
# frictionless describe ../data/csv/Mega-Sena.csv --yaml > datapackage.yaml #rodar no terminal para gerar o datapackage
# package = Package("datapackage2.yaml")
# mega = package.get_resource("mega-sena")
# df = mega.to_pandas()

# import ipdb

# ipdb.set_trace(context=10)
