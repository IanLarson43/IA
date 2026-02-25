import lightgbm
import numpy as np
import requests
from pathlib import Path
from dataset import create_dataset
from predict import predict
from train import train
from match_scrape import match_scrape
from utils import pokepaste_to_number_dict


def run_cli():
    a_input = input(
        "What do you want to do?\nPredict Results (1)\nTrain New Model (2)\n"
    )

    if a_input == "1":
        print("Choose one of the following models to use: ")
        for file in Path("models").glob("*.txt"):
            print(file.stem)
        model_name = input()
        try:
            team1 = requests.get(input("Enter team 1: ")).text
            team2 = requests.get(input("Enter team 2: ")).text
        except requests.exceptions.MissingSchema:
            print("Invalid URL")
            run_cli()
            return

        try:
            team1_list = list(pokepaste_to_number_dict(team1).values())
        except KeyError:
            print("Invalid team")
            run_cli()
            return

        try:
            team2_list = list(pokepaste_to_number_dict(team2).values())
        except KeyError:
            print("Invalid team")
            run_cli()
            return

        sample1 = np.array(team1_list + team2_list).reshape(1, -1)
        sample2 = np.array(team2_list + team1_list).reshape(1, -1)

        try:
            print(
                "Team 1 win probability: "
                + str(predict(sample1, sample2, model_name))
                + "%"
            )
        except lightgbm.basic.LightGBMError:
            print("Invalid model name")
            run_cli()
            return
    elif a_input == "2":
        a_input = input(
            "This will take a long time (Around 2 Hours). Are you sure? (y/n)\n"
        )
        if a_input.lower() == "y":
            file_name = input("Enter file name for model: ")
            print("Scraping data...")
            match_scrape(100)
            print("Done")
            print("Creating dataset...")
            create_dataset()
            print("Done")
            print("Training model...")
            train(file_name)
            print("Done")

    run_cli()
    return


run_cli()
