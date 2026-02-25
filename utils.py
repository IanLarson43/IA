import json


def clean_string(string):
    return string.replace(" ", "").replace("-", "").replace("'", "")


def pokepaste_to_number_dict(paste):
    team_list = []

    for line in paste.split("\n"):
        line = line.strip()
        if line.startswith("<span"):
            output = ""
            split_line = line.split()[2:]

            if split_line[0] == "Type:":
                output = split_line[-1]

                if output.startswith("<"):
                    output = "Stellar"
                    team_list.append(output)
                else:
                    output = output.split(">")[1].split("<")[0]
                    team_list.append(output)
            elif split_line[0].startswith("<"):
                for word in split_line:
                    if word.startswith("<"):
                        output += word.split(">")[1]
                    else:
                        output += word
                # Don't include level
                try:
                    int(output)
                except ValueError:
                    team_list.append(clean_string(output))
            else:
                for word in split_line:
                    output += word
                team_list.append(clean_string(output))

        if line.startswith("<pre"):
            name = ""
            item = ""
            temp_list = line.split()

            if "@" in temp_list:
                index = temp_list.index("@")
            else:
                index = 1

            temp_name_list = temp_list[0:index]
            if len(temp_name_list[0]) == 10:
                temp_name_list.pop(0)
            name_list = temp_name_list[0].split(">")[1:]
            if len(temp_name_list) == 2:
                name_list.append(temp_name_list[1])

            if len(name_list) == 1:
                name = name_list[0]
            else:
                if name_list[1] == "":
                    name = name_list[0].split("<")[0]
                else:
                    name = name_list[0] + " " + name_list[1].split("<")[0]

            if len(temp_list) > index + 1:
                item_list = temp_list[index + 1 :]
                item = ""
                for word in item_list:
                    item += word
            else:
                item = "None"

            team_list.append(name)
            team_list.append(clean_string(item))

        if line.startswith("-"):
            split_line = line.split()[1:]
            move = ""

            for word in split_line:
                move += word

            team_list.append(clean_string(move))
    team_dict = get_all_dict()
    for i in team_list:
        team_dict[i] += 1
    return team_dict


def get_all_dict():
    a_dict = pokemon_file.copy()
    a_dict.update(ability_file)
    a_dict.update(item_file)
    a_dict.update(move_file)
    a_dict.update(tera_dict)
    return a_dict


pokemon_file = json.load(open("data/pokemon_data.json"))
ability_file = json.load(open("data/ability_data.json"))
item_file = json.load(open("data/item_data.json"))
move_file = json.load(open("data/move_data.json"))
tera_dict = {
    "Normal": 0,
    "Fire": 0,
    "Water": 0,
    "Electric": 0,
    "Grass": 0,
    "Ice": 0,
    "Fighting": 0,
    "Poison": 0,
    "Ground": 0,
    "Flying": 0,
    "Psychic": 0,
    "Bug": 0,
    "Rock": 0,
    "Ghost": 0,
    "Dragon": 0,
    "Dark": 0,
    "Steel": 0,
    "Fairy": 0,
    "Stellar": 0,
}
