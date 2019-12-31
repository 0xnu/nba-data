# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 19:35:35 2019
author: Finbarrs Oketunji
"""

import requests
import simplejson as json
import pandas as pd

url = 'https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=Totals&Scope=S&Season=2019-20&SeasonType=Regular+Season&StatCategory=FG3M'
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36'
headers = {'User-Agent': user_agent}
players = requests.get(url, headers=headers)
data = players.json()

# Dump data
with open('./data/players.json', 'w') as f:
    json.dump(data, f)

# Convert to .json to .csv
df = pd.DataFrame(data['resultSet']['rowSet'], columns=data['resultSet']['headers'])
df.to_csv('./data/players.csv', index=False)