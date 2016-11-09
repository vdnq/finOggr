from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

url = 'http://finviz.com/screener.ashx?v={}'

html = urlopen(url).read()

bs_obj = BeautifulSoup(html, "html.parser")
companies = bs_obj.find_all('a', {'class': 'screener-link-primary'})
industries = bs_obj.find_all('a', {'class': 'screener-link'})

stuff = bs_obj.find_all('td', {'class': 'screener-body-table-nw', 'align': 'left', 'title': re.match()})
print(stuff)

