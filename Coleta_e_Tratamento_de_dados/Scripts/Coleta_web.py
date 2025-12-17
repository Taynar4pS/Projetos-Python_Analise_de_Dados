import requests
from bs4 import BeautifulSoup

url = 'https://python.org.br/web/'
requisicao = requests.get(url)
#Extração de dados:
extracao = BeautifulSoup(requisicao.content, 'html.parser')

#Exibir texto. .Strip: Remove os espaços em branco
print(extracao.text.strip())
#Criar var. de contar
contar_titulos = 0
contar_paragrafos = 0

#Filtrar por uma tag
##Contar
for linha_texto in extracao.find_all(['h2','p']):
   if linha_texto.name == 'h2':
        contar_titulos += 1 #contar_titulos +1
    elif linha_texto.name == 'p':
        contar_paragrafos += 1


print("Total de Títulos:", contar_titulos)
print('Total de Parágrafos:', contar_paragrafos)

##Exibir texto
###for linha_texto in extracao.find_all(['h2','p']):
    ###if linha_texto.name == 'h2':
     ###   titulo = linha_texto.text.strip()
     ###   print("Títulos:", '\n', titulo)
    ###elif linha_texto.name == 'p':
     ###   paragrafo = linha_texto.text.strip()
     ###   print('Parágrafos: \n', paragrafo)
## Exibir tag alinhada (Quando em uma tag tem outra)
###for linha_texto in extracao.find_all('h2'):
    ###titulo_texto = linha_texto.text.strip()
 ###print('\n Títulos:', titulo_texto)

###for link in linha_texto.find_next_siblings('p'):
#####for a in link.find_all('a', href=True):
###print('Texto link:', a.text.strip(), 'URL:', a['href'])