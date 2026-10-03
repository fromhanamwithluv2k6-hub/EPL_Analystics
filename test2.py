import requests
import pandas as pd
from pathlib import Path
from soccerdata import Understat

BASE = Path(__file__).resolve().parent
understat = Understat(leagues="ENG-Premier League", seasons="2026/2027",no_cache = True)

def update_match_stat():
    file_csv = BASE/'data/match_stat.csv'
    df = understat.read_team_match_stats()
    if not df.empty:
        '''df_cur = pd.read_csv(file_csv)
        df_cur.iloc[0:0].to_csv(file_csv,index = False,encoding='utf-8-sig')'''
        cols = ['game_id','home_team_code','away_team_code','home_points',
                    'home_expected_points','home_goals','home_xg','home_ppda',
                    'home_deep_completions','away_points','away_expected_points',
                    'away_xg','away_ppda','away_deep_completions']
        df[cols].to_csv(file_csv,index=False,encoding='utf-8-sig')
        print('match_stat updated')
    else:
        return print('match_stat update failed')
update_match_stat()