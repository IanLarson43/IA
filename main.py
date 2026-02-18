import json

item_file = json.load(open("data/item_data.json"))
move_file = json.load(open("data/move_data.json"))


class Team:
    def __init__(self, team_list):
        self.mons = []
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

                self.mons.append(
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
