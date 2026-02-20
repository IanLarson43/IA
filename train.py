import lightgbm as lgb
import json
import numpy as np

matchups_file = np.load("data/matchups.npz")
winner_file = np.load("data/winner.npz")

file = open("data/model.json")

param = {}
num_round = 10

train_data = []
validation_data = []

for match in matchups_file:
    train_data.append(matchups_file[match])
    validation_data.append(winner_file[match])

    cat_indices = []
    for i in range(len(train_data)):
        cat_indices.append(i)

train_set = lgb.Dataset(train_data, label=validation_data, categorical_feature=cat_indices)

bst = lgb.train(param, train_set, num_round)

json_model = bst.dump_model()
json.dump(json_model, file, indent=4)