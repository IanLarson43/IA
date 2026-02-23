import lightgbm as lgb
import numpy as np


def predict(sample1, sample2, model_name):
    bst = lgb.Booster(model_file=f"models/{model_name}.txt")

    prediction1 = bst.predict(sample1)[0] * 100
    prediction2 = bst.predict(sample2)[0] * 100
    return (prediction1 + (1 - prediction2)) / 2


matchups_file = np.load("data/matchups.npz")
winner_file = np.load("data/winner.npz")
