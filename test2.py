import requests
import pandas as pd
from pathlib import Path
from soccerdata import Understat

BASE = Path(__file__).resolve().parent
understat = Understat(leagues="ENG-Premier League", seasons="2026/2027",no_cache = True)

with open(BASE/'.gitignore/API_KEY.txt','r',encoding = 'utf-8') as f:
            API_KEY = f.readline()

def update_teams():
    url = "https://api.football-data.org/v4/competitions/PL/teams"
    headers = {"X-Auth-Token": API_KEY}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        file_csv = BASE/'data/teams.csv'
        data = response.json()
        teams = data["teams"]
        team_names = sorted(t["tla"] for t in teams)
        team_ids = {name: team_id for team_id, name in enumerate(team_names, start=1)}
        df = pd.DataFrame([{
               'Team_id' : team_ids[t['tla']],
               'Team' : t['name'],
               'Founded' : t['founded'],
                'Home_stadium' : t['venue'],
                'Logo_url' : t['crest']
        }for t in teams])
        df_cur = pd.read_csv(file_csv)
        df_cur.iloc[0:0].to_csv(file_csv,index=False,encoding='utf-8-sig')
        df.to_csv(file_csv,index=False,encoding='utf-8-sig')
        print('teams updated')
    else:
        print('teams update failed')
update_teams()