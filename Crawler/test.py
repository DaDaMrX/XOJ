from bs4 import BeautifulSoup
import re

html = open('C:\\Users\\DaDa\\Google Drive\\XOJ\\Crawler\\table.html').read()
soup = BeautifulSoup(html, 'lxml')
table = soup.find('table', class_ = 'a')
tr = table.find_all('tr')[1]
td = tr.find_all('td')[3]
text = td.find(text = re.compile('[A.c, C.m]'))

print(text)