import json
import requests
import time
from main import Team

file = open("data/match_data.json", "w")
matches = []

for page in range(1, 2):
    replays_data = requests.get(f"https://replay.pokemonshowdown.com/search.json?format=gen9vgc2026regfbo3&page={page}").json()
    for match in replays_data:
        id = match["id"]
        data = (requests.get(f"https://replay.pokemonshowdown.com/{id}.json").json())["log"]
        split_data = data.split("\n")
        player = 1
        for line in split_data:
            if line.startswith("|player|p1|"):
                p1_name = line.split("|")[3]
            if line.startswith("|player|p2|"):
                p2_name = line.split("|")[3]

            if line.startswith("|showteam"):
                temp_list = []
                line = line.replace("]", "|")
                for i in line.split("|")[2:]:
                    if not (i == "" or i == "M" or i == "F" or i == "50"):
                        temp_list.append(i)
                if player == 1:
                    p1_team = Team(temp_list)
                    player = 2
                else:
                    p2_team = Team(temp_list)
                    player = 1   

            if line.startswith("|win|"):
                winner_name = line.split("|")[2]
                if winner_name == p1_name:
                    winner = 1
                if winner_name == p2_name:
                    winner = 2
            
        matches.append({"p1 team" : p1_team.mons, "p2 team" : p2_team.mons, "winner" : winner})
        time.sleep(1)  
        
json.dump(matches, file, indent = 4)
file.close()