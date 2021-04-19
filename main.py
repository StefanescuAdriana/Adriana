import requests
from bs4 import BeautifulSoup
URL = 'https://www.calitateaer.ro/public/home-page/?__locale=ro'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())
