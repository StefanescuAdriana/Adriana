import requests
from bs4 import BeautifulSoup
import re

URL = 'https://www.calitateaer.ro/public/management-page/management-page/?__locale=ro'

page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

consilii = re.findall(r'[j]\w{3,}\s\w{3,}', soup.prettify())
for consilii in consilii:
    print(consilii)

#print(soup.prettify())
