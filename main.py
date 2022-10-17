import collections
from multiprocessing.spawn import import_main_path
from urllib.request import urlopen, Request
import  json
from PyPDF2 import PdfFileReader
import io
import  pandas as pd

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

df = pd.DataFrame([], columns=['nom_barri', 'poblacio_sola', 'titulats_superiors', 'nombre_aturats' , 'renda', 'sobreenvelliment'])

for x in range(73):
    barri = parser[x]
    NB = barri['NOM_DIVISIO_TERRITORIAL']
    barri_pdf = barri['URL_FITXA_DIVISIO_TERRITORIAL']
    #print(barri_name)
    #print(barri_pdf)
    pdf = urlopen(Request(barri_pdf)).read()
    memory_file = io.BytesIO(pdf)
    pdf_file = PdfFileReader(memory_file)
    page = pdf_file.getPage(1)
    page_content = page.extract_text()
    i = page_content.find('Població de més de 65 anys que viu sola (%)  (2)')
    PS = page_content[(i + 49):page_content.find(' ', i + 49)]
    i = page_content.find('% Titulats superiors i CFGS (1)')
    TS = page_content[(i + 32):page_content.find(' ', i + 32)]
    i = page_content.find("Nombre d'aturats registrats (5)")
    NA = page_content[(i + 32):page_content.find(' ', i + 32)]
    i = page_content.find("Renda familiar disponible per habitant (2017)")
    RF = page_content[(i + 46):page_content.find(' ', i + 46)]
    i = page_content.find("Índex de sobreenvelliment   (3)")
    IS = page_content[(i + 32):page_content.find(' ', i + 32)]
    df1 = pd.DataFrame([[NB, PS, TS, NA, RF, IS]], columns=['nom_barri', 'poblacio_sola', 'titulats_superiors', 'nombre_aturats' , 'renda', 'sobreenvelliment'])
    df = pd.concat([df, df1])
df.to_csv('data.csv', index=False)
