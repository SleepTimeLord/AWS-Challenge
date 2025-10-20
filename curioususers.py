import pandas as pd


def get_curious_users(output):
    df = pd.read_json(r"outputs\output4.jsonl", lines=True, encoding="utf-16")

    filterByFailedEntry = df[df["success"] == False]

    # get only unique values
    curiousUsers = filterByFailedEntry["user_id"].unique()

    print(f"Amount of users that have failed to access rooms that they are not authorized to access {len(curiousUsers)}")
    print(curiousUsers)

get_curious_users(r"outputs\output4.jsonl")