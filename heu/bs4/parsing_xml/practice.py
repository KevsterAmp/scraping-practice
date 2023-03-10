import requests
from bs4 import BeautifulSoup

url = 'https://www.vice.com/en/sitemap/'
r = requests.get(url)
print(r.content)
sp = BeautifulSoup(r.text, 'lxml')
links = sp.find_all('loc')
print(len(links))
