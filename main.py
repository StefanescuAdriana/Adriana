from bs4 import BeautifulSoup
import requests
from openpyxl import Workbook
import csv

#--------------------Preluam HTML-ul-------------------------------------------

url = 'https://www.calitateaer.ro/public/management-page/management-page/?__locale=ro'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify())

#--------------------Creeam fisierul pentru stocarea datelor-------------------

filename = 'test.csv'
f = open(filename, "w", encoding="utf-8")
f.write("datele preluate sunt: "+"\n")

#--------------------Dam scrape la datele din tabel folosind datele din HTMl------

for heading in soup.find_all('h3', class_='post-title'):
    print(heading.text)
    f.write(heading.text)

    for tr in soup.find_all('tr'):
        print(tr.text)
        f.write(tr.text)

#-------------------------------Creeam fisierul XSlX----------------------------------

wb = Workbook()
ws = wb.active
with open('test.csv', 'r+', encoding="utf-8") as f:
    for row in csv.reader(f):
        ws.append(row)
wb.save('name.xlsx')
