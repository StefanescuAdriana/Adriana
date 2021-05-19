from bs4 import BeautifulSoup
import requests
from openpyxl import Workbook
import csv
import pandas as pd

#--------------------Preluam HTML-ul-------------------------------------------

url = 'https://www.calitateaer.ro/public/management-page/management-page/?__locale=ro'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify())

#--------------------Creeam fisierul pentru stocarea datelor-------------------

filename = 'tabel.csv'
f = open(filename, "w", encoding="utf-8")
f.write("Datele preluate sunt: "+"\n")

#---------------------Al doilea fisier ajutator pentru stocare-----------------

filename = 'tabel2.csv'
g = open(filename, "w", encoding="utf-8")

#--------------------Dam scrape la datele din tabel folosind datele din HTMl------

for heading in soup.find_all('h3', class_='post-title'):
    #print(heading.text + "\t")
    f.write(heading.text)

    for aer_table in soup.find_all('table', class_='table table-striped table-bordered'):

        for table_bod in aer_table.find_all('tbody'):
            rows = table_bod.find_all('tr')

            for tr in rows:
                locatii = tr.find('td', class_= 'text-center')
                #print(tr.text)
                f.write(tr.text)

#---------------------- Mai luam datele pentru o noua prelucrare----------------------

for heading in soup.find_all('h3', class_='post-title'):
    print(heading.text + "\t")
    g.write(heading.text+"\n")
    print()

for tbod in soup.find_all('tr'):
    valori = [dt.text for dt in tbod.find_all('p')]
    print(valori)
    g.write(str(valori)+"\n")

for tr in soup.find_all('tr'):
    values = [td.text for td in tr.find_all('td')]
    print(values)
    g.write(str(values)+"\n")

#-------------------------------Creeam fisierul XSlX----------------------------------

wb = Workbook()
ws = wb.active
with open('tabel.csv', 'r+', encoding="utf-8") as f:
    for row in csv.reader(f):
        ws.append(row)
wb.save('tabel.xlsx')

with open('tabel2.csv', 'r+', encoding="utf-8") as g:
    for row in csv.reader(g):
        ws.append(row)
wb.save('tabel2.xlsx')
