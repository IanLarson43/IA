import json
import numpy as np
from sklearn.preprocessing import LabelEncoder

dataset_dict = {}

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

for match in range(len(match_file)):
    match_dataset = []
    for mon in match_file[match]["p1 team"]:
        match_dataset.append(mon["name"])
        match_dataset.append(mon["item"])
        match_dataset.append(mon["ability"])
        for move in mon["moves"]:
            match_dataset.append(move)
        match_dataset.append(mon["tera"])

    for mon in match_file[match]["p2 team"]:
        match_dataset.append(mon["name"])
        match_dataset.append(mon["item"])
        match_dataset.append(mon["ability"])
        for move in mon["moves"]:
            match_dataset.append(move)
        match_dataset.append(mon["tera"])

    encoded_match_dataset = []
    for i in match_dataset:
        if i in pokemon_file:
            encoded_match_dataset.append(pokemon_encoder.transform([i])[0])
        elif i in ability_file:
            encoded_match_dataset.append(ability_encoder.transform([i])[0])
        elif i in item_file:
            encoded_match_dataset.append(item_encoder.transform([i])[0])
        elif i in move_file:
            encoded_match_dataset.append(move_encoder.transform([i])[0])
    encoded_match_dataset.append(match_file[match]["winner"])

    dataset_dict[f"match {match}"] = encoded_match_dataset

np.savez("data/dataset.npz", **dataset_dict)
