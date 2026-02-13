import json
from sklearn.preprocessing import LabelEncoder

pokemon_file = json.load(open("data/pokemon_data.json"))
ability_file = json.load(open("data/ability_data.json"))
item_file = json.load(open("data/item_data.json"))
move_file = json.load(open("data/move_data.json"))
match_file = json.load(open("data/match_data.json"))

pokemon_list = []
for mon in pokemon_file.keys():
    pokemon_list.append(mon)

pokemon_encoder = LabelEncoder()
ability_encoder = LabelEncoder()
item_encoder = LabelEncoder()
move_encoder = LabelEncoder()

pokemon_encoder.fit(pokemon_list)
ability_encoder.fit(ability_file)
item_encoder.fit(item_file)
move_encoder.fit(move_file)

for i in match_file:
    for j in i:
        match_dataset = []
        for mon in j["p1 team"]:
            match_dataset.append(mon["name"])
            match_dataset.append(mon["item"])
            match_dataset.append(mon["ability"])
            for move in mon["moves"]:
                match_dataset.append(move)
            match_dataset.append(mon["tera"])