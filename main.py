class Team:
    def __init__(self, team_list):
        self.mons = []
        for i in range(1, len(team_list), 5):
            name = team_list[i]
            item = team_list[i+1]
            ability = team_list[i+2]
            moves = team_list[i+3].split(",")
            tera = team_list[i+4].strip(",")
            self.mons.append({
                "name": name,
                "item": item,
                "ability": ability,
                "moves": moves,
                "tera": tera
            })