import json
import requests
import time

def create_team(team_list):
    mons = []
    count = 1
    done = False
    while not done:
        try:
            mon_name = team_list[count]
            count += 1
            if team_list[count] in item_file:
                mon_item = team_list[count]
                count += 1
            else:
                mon_item = "None"
            mon_ability = team_list[count]
            count += 1
            mon_moves = []
            for move in team_list[count].split(","):
                if move in move_file:
                    mon_moves.append(move)
                count += 1
            while len(mon_moves) < 4:
                mon_moves.append("None")
            mon_tera = team_list[count].strip(",")
            count += 1

            mons.append(
                {
                    "name": mon_name,
                    "item": mon_item,
                    "ability": mon_ability,
                    "moves": mon_moves,
                    "tera": mon_tera,
                }
            )
        except IndexError:
            done = True
file = open("data/match_data.json", "w")
item_file = json.load(open("data/item_data.json"))
move_file = json.load(open("data/move_data.json"))
matches = []

for page in range(1, 2):
    replays_data = requests.get(
        f"https://replay.pokemonshowdown.com/search.json?format=gen9vgc2026regfbo3&page={page}"
    ).json()
    for match in replays_data:
        id = match["id"]
        print(id)
        data = (requests.get(f"https://replay.pokemonshowdown.com/{id}.json").json())[
            "log"
        ]
        split_data = data.split("\n")
        player = 0
        for line in split_data:
            if line.startswith("|player|p1|"):
                p0_name = line.split("|")[3]
            if line.startswith("|player|p2|"):
                p1_name = line.split("|")[3]

            if line.startswith("|showteam"):
                temp_list = []
                line = line.replace("]", "|")
                for i in line.split("|")[2:]:
                    if not (i == "" or i == "M" or i == "F" or i == "50"):
                        temp_list.append(i)
                if player == 0:
                    p1_team = create_team(temp_list)
                    player = 1
                else:
                    p2_team = create_team(temp_list)
                    player = 0

            if line.startswith("|win|"):
                winner_name = line.split("|")[2]
                if winner_name == p0_name:
                    winner = 0
                if winner_name == p1_name:
                    winner = 1

        matches.append(
            {"p0 team": p1_team.mons, "p1 team": p2_team.mons, "winner": winner}
        )
        time.sleep(1)

json.dump(matches, file, indent=4)
file.close()
