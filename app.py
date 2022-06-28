from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/list_campaigns')
def index():
  con = sqlite3.connect('vamp.db')
  cur = con.cursor()
  cur.execute('''
    SELECT campaigns.name, start_date, end_date, budget, hashtags, teams.name, description
    FROM campaigns
    JOIN teams ON teams.id = team_id
  ''')
  campaigns = [
    {
      'name': name,
      'startDate': start_date,
      'endDate': end_date,
      'budget': budget,
      'hashtags': hashtags,
      'teamName': team_name,
      'description': description
    }
    for name, start_date, end_date, budget, hashtags, team_name, description in cur.fetchall()
  ]
  con.close()
  return jsonify(campaigns)
