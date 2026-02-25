import json
import requests
from utils import clean_string


file = open("data/pokemon_data.json", "w")
raw_data = requests.get("https://play.pokemonshowdown.com/data/pokedex.json").json()
data = {}

for mon in raw_data:
    data[raw_data[mon]["name"]] = 0

    try:
        for form in raw_data[mon]["cosmeticFormes"]:
            data[form] = 0
    except KeyError:
        pass

json.dump(data, file, indent=4)

file = open("data/move_data.json", "w")
raw_data = requests.get("https://play.pokemonshowdown.com/data/moves.json").json()
data = {}

for move in raw_data:
    move = clean_string(raw_data[move]["name"])
    data[move] = 0

json.dump(data, file, indent=4)

file = open("data/item_data.json", "w")
raw_data = requests.get("https://play.pokemonshowdown.com/data/items.js").text
data = {}

split_raw_data = raw_data.split('name:"')
for line in split_raw_data:
    if not line.startswith("exports.BattleItems"):
        split_line = line.split('"')
        item = clean_string(split_line[0])
        data[item] = 0

json.dump(data, file, indent=4)

file = open("data/ability_data.json", "w")
raw_data = requests.get("https://play.pokemonshowdown.com/data/abilities.js").text
data = {}

split_raw_data = raw_data.split('name:"')
for line in split_raw_data:
    if not line.startswith("exports.BattleAbilities"):
        split_line = line.split('"')
        ability = clean_string(split_line[0])
        data[ability] = 0

json.dump(data, file, indent=4)
file.close()
