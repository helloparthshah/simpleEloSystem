import sqlite3
import csv

conn = sqlite3.connect('valorant.sqlite')
conn.text_factory = str
c = conn.cursor()
data = c.execute('SELECT * FROM games')

with open('games.csv', 'w', encoding="utf-8", newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)
