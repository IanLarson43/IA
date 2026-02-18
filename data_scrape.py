import json
import requests


def clean_string(string):
    return string.replace(" ", "").replace("-", "").replace("'", "")


file = open("data/pokemon_data.json", "w")
raw_data = requests.get("https://play.pokemonshowdown.com/data/pokedex.json").json()
data = {}

data["None"] = (["None"], {"hp": 0, "atk": 0, "def": 0, "spa": 0, "spd": 0, "spe": 0})
for mon in raw_data:
    try:
        data[raw_data[mon]["name"]] = (
            raw_data[mon]["types"],
            raw_data[mon]["baseStats"],
        )

        try:
            for form in raw_data[mon]["cosmeticFormes"]:
                print(form)
                data[form] = (
                    raw_data[mon]["types"],
                    raw_data[mon]["baseStats"],
                )
        except KeyError:
            pass
    except KeyError:
        pass

json.dump(data, file, indent=4)

file = open("data/move_data.json", "w")
raw_data = requests.get("https://play.pokemonshowdown.com/data/moves.json").json()
data = []

data.append("None")
for move in raw_data:
    move = clean_string(raw_data[move]["name"])
    data.append(move)

json.dump(data, file, indent=4)

file = open("data/item_data.json", "w")
raw_data = requests.get("https://play.pokemonshowdown.com/data/items.js").text
data = []

data.append("None")
split_raw_data = raw_data.split('name:"')
for line in split_raw_data:
    if not line.startswith("exports.BattleItems"):
        split_line = line.split('"')
        item = clean_string(split_line[0])
        data.append(item)

json.dump(data, file, indent=4)

file = open("data/ability_data.json", "w")
raw_data = requests.get("https://play.pokemonshowdown.com/data/abilities.js").text
data = []

data.append("None")
split_raw_data = raw_data.split('name:"')
for line in split_raw_data:
    if not line.startswith("exports.BattleAbilities"):
        split_line = line.split('"')
        ability = clean_string(split_line[0])
        data.append(ability)

json.dump(data, file, indent=4)
file.close()
