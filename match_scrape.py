import json
import requests
import time

for page in range(1, 2):
    replays_data = requests.get(f"https://replay.pokemonshowdown.com/search.json?format=gen9vgc2026regfbo3&page={page}").json()
    for match in replays_data:
        id = match["id"]
        data = (requests.get(f"https://replay.pokemonshowdown.com/{id}.json").json())["log"]
        temp_data = data.replace("|showteam|", "~").replace("|inactive|", "~").replace("|t:|", "~")
        split_data = temp_data.split("~")
        for line in split_data:
            if line.startswith("p1") or line.startswith("p2"):
                split_line = line.split("|")
        
