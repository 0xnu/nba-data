import json
import requests
import pandas as pd

players = requests.get('https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=Totals&Scope=S&Season=2019-20&SeasonType=Regular+Season&StatCategory=FG3M')
data = players.json()
with open('./data/players.json', 'w') as f:
    json.dump(data, f)

# Convert to .json to .csv
df = pd.DataFrame(data['resultSet']['rowSet'], columns=data['resultSet']['headers'])
df.to_csv('./data/players.csv', index=False)
print('I am done scraping data. Bye!')
