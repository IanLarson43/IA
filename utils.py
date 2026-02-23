import json


def clean_string(string):
    return string.replace(" ", "").replace("-", "").replace("'", "")


def list_to_id_dict(a_list):
    a_dict = {}
    for i, name in enumerate(a_list):
        a_dict[name] = i
    return a_dict


def pokepaste_to_list(paste):
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
                    team_list.append(tera_dict[output])
                else:
                    output = output.split(">")[1].split("<")[0]
                    team_list.append(tera_dict[output])
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
                    team_list.append(ability_dict[clean_string(output)])
            else:
                for word in split_line:
                    output += word
                team_list.append(move_dict[clean_string(output)])

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

            team_list.append(pokemon_dict[name])
            team_list.append(item_dict[clean_string(item)])

        if line.startswith("-"):
            split_line = line.split()[1:]
            move = ""

            for word in split_line:
                move += word

            team_list.append(move_dict[clean_string(move)])
    return team_list


pokemon_file = json.load(open("data/pokemon_data.json"))
ability_file = json.load(open("data/ability_data.json"))
item_file = json.load(open("data/item_data.json"))
move_file = json.load(open("data/move_data.json"))

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
