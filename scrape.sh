#!/usr/bin/env bash
#chmod +x scrape.sh && ./scrape.sh

for TEAM in "ATL" "BOS" "BKN" "CHA" "CHI" "CLE" "DAL" "DEN" "DET" "GSW" "HOU" "IND" "LAC" "LAL" "MEM" "MIA" "MIL" "MIN" "NOP" "NYK" "OKC" "ORL" "PHI" "PHX" "POR" "SAC" "SAS" "TOR" "UTA" "WAS"
do
  wget "http://stats.nba.com/media/img/teams/logos/${TEAM}_logo.svg"
  cairosvg ${TEAM}_logo.svg -o ${TEAM}.png
  convert ${TEAM}.png -resize 256x256 ${TEAM}.png
done

mkdir -p ./data/logos/png; mkdir -p ./data/logos/svg
mv *.png ./data/logos/png; mv *.svg ./data/logos/svg

python3 ./players.py && python3 ./headshots.py
mv *.png ./data/players

# Push to repository
git add .
git commit -s -m "nba data"
git push

echo "I am done scraping data. Bye!"