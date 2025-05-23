import bs4
import requests

resultado= requests.get('https://www.pcfactory.cl')


sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

imagenes = sopa.select('img')
for i in imagenes:
    print(i)