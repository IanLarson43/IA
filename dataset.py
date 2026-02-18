import json
import numpy as np


def list_to_id_dict(a_list):
    a_dict = {}
    for i, name in enumerate(a_list):
        a_dict[name] = i
    return a_dict


dataset_dict = {}

pokemon_file = json.load(open("data/pokemon_data.json"))
ability_file = json.load(open("data/ability_data.json"))
item_file = json.load(open("data/item_data.json"))
move_file = json.load(open("data/move_data.json"))
match_file = json.load(open("data/match_data.json"))

pokemon_list = []
for mon in pokemon_file.keys():
    pokemon_list.append(mon)
tera_list = [
    "None",
    "Normal",
    "Fire",
    "Water",
    "Electric",
    "Grass",
    "Ice",
    "Fighting",
    "Poison",
    "Ground",
    "Flying",
    "Psychic",
    "Bug",
    "Rock",
    "Ghost",
    "Dragon",
    "Dark",
    "Steel",
    "Fairy",
    "Stellar",
]

pokemon_dict = list_to_id_dict(pokemon_list)
ability_dict = list_to_id_dict(ability_file)
item_dict = list_to_id_dict(item_file)
move_dict = list_to_id_dict(move_file)
tera_dict = list_to_id_dict(tera_list)

for match in range(len(match_file)):
    match_dataset = []
    for mon in match_file[match]["p0 team"]:
        match_dataset.append(pokemon_dict[mon["name"]])
        match_dataset.append(item_dict[mon["item"]])
        match_dataset.append(ability_dict[mon["ability"]])
        for move in range(4):
            try:
                match_dataset.append(move_dict[mon["moves"][move]])
            except IndexError:
                match_dataset.append(move_dict["None"])
        match_dataset.append(tera_dict[mon["tera"]])
    for i in range(6 - len(match_file[match]["p0 team"])):
        match_dataset.append(pokemon_dict["None"])
        match_dataset.append(item_dict["None"])
        match_dataset.append(ability_dict["None"])
        for move in range(4):
            match_dataset.append(move_dict["None"])
        match_dataset.append(tera_dict["None"])

    for mon in match_file[match]["p1 team"]:
        match_dataset.append(pokemon_dict[mon["name"]])
        match_dataset.append(item_dict[mon["item"]])
        match_dataset.append(ability_dict[mon["ability"]])
        for move in range(4):
            try:
                match_dataset.append(move_dict[mon["moves"][move]])
            except IndexError:
                match_dataset.append(move_dict["None"])
        match_dataset.append(tera_dict[mon["tera"]])
    for i in range(6 - len(match_file[match]["p1 team"])):
        match_dataset.append(pokemon_dict["None"])
        match_dataset.append(item_dict["None"])
        match_dataset.append(ability_dict["None"])
        for move in range(4):
            match_dataset.append(move_dict["None"])
        match_dataset.append(tera_dict["None"])

    match_dataset.append(match_file[match]["winner"])

    dataset_dict[f"match {match}"] = np.array(match_dataset, dtype=np.int32)

np.savez("data/dataset.npz", **dataset_dict)
