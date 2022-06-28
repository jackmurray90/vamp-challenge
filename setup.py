import sqlite3
import csv

con = sqlite3.connect('vamp.db')

cur = con.cursor()

cur.execute('''CREATE TABLE campaigns (id INTEGER, name TEXT, start_date DATE, end_date DATE, budget REAL, hashtags TEXT, team_id INTEGER, description TEXT)''')
cur.execute('''CREATE TABLE teams (id INTEGER, name TEXT, code TEXT, color_set TEXT)''')

with open('campaigns.csv', newline='') as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
    cur.execute('INSERT INTO campaigns VALUES (?, ?, ?, ?, ?, ?, ?, ?)', (row['id'], row['name'], row['start_date'], row['end_date'], row['budget'], row['hashtags'], row['team_id'], row['description']))

with open('teams.csv', newline='') as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
    cur.execute('INSERT INTO teams VALUES (?, ?, ?, ?)', (row['id'], row['name'], row['code'], row['color_set']))


con.commit()

con.close()
