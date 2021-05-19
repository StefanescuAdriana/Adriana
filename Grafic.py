import matplotlib.pyplot as plt
import csv

from main import row

Judete = []
Calitatea_aerului = []

with open('tabel2.csv', 'r') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    for lines in row:
        Judete.append(lines[0])
        Calitatea_aerului.append(int(lines[1]))

plt.pie(Calitatea_aerului, labels=Judete, autopct='%.2f%%')
plt.title('calitate aer', fontsize=20)
plt.show()