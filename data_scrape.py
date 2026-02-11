import json
import requests

file = open("data/pokemon_data.json", "w")
raw_data = requests.get("https://play.pokemonshowdown.com/data/pokedex.json").json()
data = {}

for mon in raw_data:
    try:
        data[raw_data[mon]["name"]] = (raw_data[mon]["types"], raw_data[mon]["baseStats"])

        try:
            for form in raw_data[mon]["cosmeticFormes"]:
                data[raw_data[mon][raw_data[form]]] = (raw_data[mon]["types"], raw_data[mon]["baseStats"])
        except(KeyError):
            pass
    except(KeyError):
        pass

json.dump(data, file, indent = 4)

file = open("data/move_data.json", "w")
raw_data = requests.get("https://play.pokemonshowdown.com/data/moves.json").json()
data = []

for move in raw_data:
    move = move.replace(" ", "")
    data.append(raw_data[move]["name"])

json.dump(data, file, indent = 4)

file = open("data/item_data.json", "w")
raw_data = requests.get("https://play.pokemonshowdown.com/data/items.js").text
data = []

split_raw_data = raw_data.split("name:\"")
for line in split_raw_data:
    if not line.startswith("exports.BattleItems"):
        split_line = line.split("\"")
        item = split_line[0].replace(" ", "")
        data.append(item)

json.dump(data, file, indent = 4)

file = open("data/ability_data.json", "w")
raw_data = requests.get("https://play.pokemonshowdown.com/data/abilities.js").text
data = []

split_raw_data = raw_data.split("name:\"")
for line in split_raw_data:
    if not line.startswith("exports.BattleAbilities"):
        split_line = line.split("\"")
        ability = split_line[0].replace(" ", "")
        data.append(ability)

json.dump(data, file, indent = 4)
file.close()