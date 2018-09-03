import urllib.request
import shutil

url = 'http://bsi.uniriotec.br/alunos/matriculas/Alunos_SI_2018.1.pdf'
response = urllib.request.urlopen(url)
data = response.read()      # a `bytes` object
file_name = 'alunos.pdf'

with urllib.request.urlopen(url) as response, open(file_name, 'wb') as out_file:
    shutil.copyfileobj(response, out_file)
