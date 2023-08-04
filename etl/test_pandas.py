from frictionless import Package
import pandas as pd

# df = pd.read_excel("jogos/Mega-Sena.xlsx", index_col=0)
# df.to_csv("jogos/Mega-Sena.csv")


package = Package("datapackage2.yaml")
mega = package.get_resource("mega-sena")
df = mega.to_pandas()

import ipdb

ipdb.set_trace(context=10)
