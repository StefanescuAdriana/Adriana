import requests
from bs4 import BeautifulSoup
import re

URL = 'https://www.calitateaer.ro/public/management-page/management-page/?__locale=ro'

page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

consilii = re.findall(r'[C]\w{7,12}\s\w{3,}\s\w{3,}', soup.prettify())
for consilii in consilii:
    print(consilii)

f = open("consil.txt", "w")
for consilii in consilii:
    f.write(consilii+"\n")

#print(soup.prettify())
