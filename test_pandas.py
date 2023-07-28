from frictionless import Package
package = Package('datapackage.yaml')
mega = package.get_resource('mega-sena')
df = mega.to_pandas()
import ipdb; ipdb.set_trace(context=10)
