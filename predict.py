import lightgbm as lgb


def predict(sample1, sample2, model_name):
    bst = lgb.Booster(model_file=f"models/{model_name}.txt")

    prediction1 = bst.predict(sample1)[0]
    prediction2 = bst.predict(sample2)[0]

    return ((prediction1 + (1 - prediction2)) / 2) * 100
