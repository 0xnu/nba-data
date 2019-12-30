#!/usr/bin/env bash

mkdir -p ./player_data
python3 ./players.py
find player_data -name '*.json' -exec cat {} \; | jq --slurp . -c > players.json
#mkdir -p ./data; mv players.json $_
mkdir -p ./data; mv players.json ./data
rm -rf player_data

echo "I am done scraping data. Bye!"
