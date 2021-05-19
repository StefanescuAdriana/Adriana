import matplotlib.pyplot as plt
import csv

from main import row

Subjects = []
Scores = []

with open('tabel2.csv', 'r') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    for lines in row:
        Subjects.append(lines[0])
        Scores.append(int(lines[1]))

plt.pie(Scores, labels=Subjects, autopct='%.2f%%')
plt.title('calitate aer', fontsize=20)
plt.show()