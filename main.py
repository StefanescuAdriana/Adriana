import requests
from bs4 import BeautifulSoup
#<import requests>
from openpyxl import Workbook
import csv
import pandas as pd


#--------------------Preluam HTML-ul-------------------------------------------

url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSbYNXVk7ANiY9Kh5hAkL8wcrP98PLz-HluUSlThK2zd688Yf1jARgYfbI-vWeVRPSgZ0Xs3OtRJcrm/pubhtml?gid=986640458&single=true'
page = requests.get(url)
print(page.content)
soup = BeautifulSoup(page.content, 'html.parser')
#cauta toate tag-urile cu numele table si le returneaza intr-o lista
table = soup.find_all()
print(table)
table = pd.read_html(url,encoding='utf-8')[1]
table.to_csv('date.csv')
#convertim csv-ul in excel
wb = Workbook()
ws = wb.active
with open('../../../Desktop/date.csv', 'r', encoding="utf-8") as f:
    for row in csv.reader(f):
        ws.append(row)
wb.save('data.xlsx')
