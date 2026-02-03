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

json.dump(data, file)
