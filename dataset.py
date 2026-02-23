import json
import numpy as np
from utils import pokemon_dict, item_dict, ability_dict, move_dict, tera_dict

matchup_dict = {}
winner_dict = {}

match_file = json.load(open("data/match_data.json"))

for match in range(len(match_file)):
    match_dataset = []
    flipped_match_dataset = []
    p0_dataset = []
    p1_dataset = []

    for mon in match_file[match]["p0 team"]:
        p0_dataset.append(pokemon_dict[mon["name"]])
        p0_dataset.append(item_dict[mon["item"]])
        p0_dataset.append(ability_dict[mon["ability"]])
        for move in range(4):
            try:
                p0_dataset.append(move_dict[mon["moves"][move]])
            except IndexError:
                p0_dataset.append(move_dict["None"])
        p0_dataset.append(tera_dict[mon["tera"]])
    for i in range(6 - len(match_file[match]["p0 team"])):
        p0_dataset.append(pokemon_dict["None"])
        p0_dataset.append(item_dict["None"])
        p0_dataset.append(ability_dict["None"])
        for move in range(4):
            p0_dataset.append(move_dict["None"])
        p0_dataset.append(tera_dict["None"])

    for mon in match_file[match]["p1 team"]:
        p1_dataset.append(pokemon_dict[mon["name"]])
        p1_dataset.append(item_dict[mon["item"]])
        p1_dataset.append(ability_dict[mon["ability"]])
        for move in range(4):
            try:
                p1_dataset.append(move_dict[mon["moves"][move]])
            except IndexError:
                p1_dataset.append(move_dict["None"])
        p1_dataset.append(tera_dict[mon["tera"]])
    for i in range(6 - len(match_file[match]["p1 team"])):
        p1_dataset.append(pokemon_dict["None"])
        p1_dataset.append(item_dict["None"])
        p1_dataset.append(ability_dict["None"])
        for move in range(4):
            p1_dataset.append(move_dict["None"])
        p1_dataset.append(tera_dict["None"])

    match_dataset = p0_dataset + p1_dataset
    flipped_match_dataset = p1_dataset + p0_dataset

    matchup_dict[f"match {match}"] = np.array(match_dataset, dtype=np.int64)
    matchup_dict[f"match {match} flipped"] = np.array(
        flipped_match_dataset, dtype=np.int64
    )
    winner_dict[f"match {match}"] = np.array(
        match_file[match]["winner"], dtype=np.int64
    )
    winner_dict[f"match {match} flipped"] = np.array(
        1 - match_file[match]["winner"], dtype=np.int64
    )


np.savez("data/matchups.npz", **matchup_dict)
np.savez("data/winner.npz", **winner_dict)
