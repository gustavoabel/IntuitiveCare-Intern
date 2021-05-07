import re
from wget import download
from urllib.request import urlopen
from bs4 import BeautifulSoup

def scrape(url):
    page = urlopen(url)
    html = page.read().decode("utf-8")
    return BeautifulSoup(html, "html.parser")
               
               
base_url = 'http://www.ans.gov.br'

tiss_url = base_url + '/prestadores/tiss-troca-de-informacao-de-saude-suplementar'
tiss_html = scrape(tiss_url)

# pega o link que contém a palavra versão
padrao_tiss_href = tiss_html.find(string=re.compile('versão')).parent.get('href')
padrao_tiss_url = base_url + padrao_tiss_href
padrao_tiss_html = scrape(padrao_tiss_url)

# pega o link que termina com .pdf
pdf_href = padrao_tiss_html.find('a', attrs={'href': re.compile(".pdf$")}).get('href')
pdf_url = base_url + pdf_href
download(pdf_url)