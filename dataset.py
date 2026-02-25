import json
import numpy as np
from utils import get_all_dict

pokemon_file = json.load(open("data/pokemon_data.json"))
ability_file = json.load(open("data/ability_data.json"))
item_file = json.load(open("data/item_data.json"))
move_file = json.load(open("data/move_data.json"))


def create_dataset():
    match_file = json.load(open("data/match_data.json"))

    matchup_dict = {}
    winner_dict = {}

    for match in range(len(match_file)):
        match_dataset = {}
        flipped_match_dataset = {}

        p0_dict = get_all_dict()
        p1_dict = get_all_dict()

        for mon in match_file[match]["p0 team"]:
            p0_dict[mon["name"]] += 1
            p0_dict[mon["ability"]] += 1
            try:
                p0_dict[mon["item"]] += 1
            except KeyError:
                pass
            p0_dict[mon["ability"]] += 1
            for move in mon["moves"]:
                p0_dict[move] += 1
            p0_dict[mon["tera"]] += 1

        for mon in match_file[match]["p1 team"]:
            p1_dict[mon["name"]] += 1
            p1_dict[mon["ability"]] += 1
            try:
                p1_dict[mon["item"]] += 1
            except KeyError:
                pass
            p1_dict[mon["ability"]] += 1
            for move in mon["moves"]:
                p1_dict[move] += 1
            p1_dict[mon["tera"]] += 1

        match_dataset = list(p0_dict.values()) + list(p1_dict.values())
        flipped_match_dataset = list(p1_dict.values()) + list(p0_dict.values())

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

    np.savez_compressed("data/matchups.npz", **matchup_dict)
    np.savez_compressed("data/winner.npz", **winner_dict)
