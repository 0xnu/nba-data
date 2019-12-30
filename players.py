import sys
import requests
import ujson as json
import pandas as pd

players = requests.get('https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=Totals&Scope=S&Season=2019-20&SeasonType=Regular+Season&StatCategory=FG3M')
data = players.json()

with open('./data/players.json', 'w') as f:
    json.dump(data, f)
except:
    print(e)

# Convert to .json to .csv
df = pd.DataFrame(data['resultSet']['rowSet'], columns=data['resultSet']['headers'])
df.to_csv('./data/players.csv', index=False)

