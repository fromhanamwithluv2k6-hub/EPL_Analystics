import requests
import pandas as pd
from pathlib import Path

BASE = Path(__file__).resolve().parent
FPL_url = "https://fantasy.premierleague.com/api/bootstrap-static/"

response = requests.get(FPL_url)
data = response.json()

with open(BASE/'.gitignore/API_KEY.txt','r',encoding = 'utf-8') as f:
    API_KEY = f.readline()

def update_standings():
    url = "https://api.football-data.org/v4/competitions/PL/standings"
    headers = {"X-Auth-Token": API_KEY}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        file_csv = BASE/'data/standings.csv'
        '''df_cur = pd.read_csv(file_csv)
        df_cur.iloc[0:0].to_csv(file_csv,index = False,encoding = 'utf-8')'''
        data = response.json()
        teams = data["standings"][0]["table"]
        team_names = sorted(t["team"]["tla"] for t in teams)
        team_ids = {name: team_id for team_id, name in enumerate(team_names, start=1)}
        df = pd.DataFrame([{
            "Team_id" : team_ids[t["team"]["tla"]],
            "Position": t["position"],
            "Team": t["team"]["name"],
            "Short Name": t["team"]["tla"],
            "Played": t["playedGames"],
            "Won": t["won"],
            "Draw": t["draw"],
            "Lost": t["lost"],
            "Goals For": t["goalsFor"],
            "Goals Against": t["goalsAgainst"],
            "Points": t["points"],
        } for t in teams])
        df.to_csv(file_csv, index=False, encoding="utf-8")
        print('done')
    else:
        print(f'error {response.status_code}')
def update_players_stat():
    file_csv = BASE/'data/players_stat.csv'
    players = data['elements']
    stat_cols = ['id']
    pos_df = ['NONE','GK','DF','MF','FW']
    df_stat = pd.DataFrame([{
        'player_id': p['id'],'player': p['web_name'],'pos' : pos_df[p['element_type']],
        'starts': p['starts'],
        'minutes' :p['minutes'],
        'yellow_cards':p['yellow_cards'],
        'red_cards':p['red_cards'],
        'og' : p['own_goals'],

        'pen_missed' : p['penalties_missed'],
        'goals' : p['goals_scored'],'xG' : p['expected_goals'],
        'assists' : p['assists'],'xA' : p['expected_assists'],
        'xGI' : p['expected_goal_involvements'],

        'clean_sheets' : p['clean_sheets'],
        'goals_conceded' : p['goals_conceded'],'xGC':p['expected_goals_conceded_per_90'],
        'CBI' : p['clearances_blocks_interceptions'],
        'recoveries' : p['recoveries'],
        'tackles' : p['tackles'],
        'defensive_contribution' : p['defensive_contribution'],

        'influence_rank' : p['influence_rank'],
        'creativity' : p['creativity'],'creativity_rank' : p['creativity_rank_type'],
        'threat' : p['threat'],'threat_rank' : p['threat_rank_type'],
        'ict_index_rank' : p['ict_index_rank_type']

    }for p in players])
    
    df_stat.to_csv(file_csv,index=False,encoding='utf-8-sig')
    print('done')
def update_players_profile():
    file_csv = BASE/'data/players_profile.csv'
    teams_csv = BASE/'data/teams.csv'
    players = data['elements']
    pos_df = ['None','GK','DF','MF','FW']
    ref_data = pd.read_csv(teams_csv)
    teams = ref_data.set_index('Team_id')['Short Name'].to_dict()
    df_profile = pd.DataFrame([{
        'player_id':p['id'],
        'player' : f'{p['first_name']} {p['second_name']}',
        'team' : teams[p['team']],
        'pos': pos_df[int(p['element_type'])],
        'photo_url'  : f"https://resources.premierleague.com/premierleague/photos/players/110x140/p{p['photo'].replace('.jpg', '.png')}"
    }for p in players])
    df_cur = pd.read_csv(file_csv)
    df_cur.iloc[0:0].to_csv(file_csv,index = False,encoding = 'utf-8_sig')
    df_profile.to_csv(file_csv,index=False,encoding='utf-8-sig')
    print('players_profile.csv updated')
if response.status_code != 200:
    print('cant connect to FPL_API')
else:
    print('ok')
def update_schedule():
    file_csv = BASE/'data/schedule.csv'