import lightgbm as lgb
import json
import numpy as np

file = np.load("data/dataset.npz")
param = {}
num_round = 10

train_data = []
validation_data = []

for match in file:
    teams = file[match][:-1]
    result = file[match][-1].item()

    train_data.append(teams)
    validation_data.append(result)

print(train_data)
bst = lgb.train(param, train_data, num_round, valid_sets=[validation_data])

json_model = bst.dump_model()
json.dump(json_model, file, indent=4)