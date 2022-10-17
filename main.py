from multiprocessing import Barrier
from urllib.request import urlopen
import  json

basicurl = 'https://opendata-ajuntament.barcelona.cat/data'
url = 'https://opendata-ajuntament.barcelona.cat/data/api/action/datastore_search?resource_id=ed515bb8-502b-4dff-96dc-769f72767919&limit=5&q=title:jones'

fileobj = urlopen(url)
parse_json = json.loads(fileobj.read().decode(fileobj.info().get_param('charset') or 'utf-8'))

start = parse_json['result']['_links']['start']

starturl = basicurl + start
starturl = starturl.replace('q=title%3Ajones&limit=5', '')
startobj = urlopen(starturl)

parse_start = json.loads(startobj.read())

parser = parse_start['result']['records']

for x in range(73):
    barri = parser[x]
    barri_name = barri['NOM_DIVISIO_TERRITORIAL']
    barri_pdf = barri['URL_FITXA_DIVISIO_TERRITORIAL']
    print(barri_name)
    print(barri_pdf)