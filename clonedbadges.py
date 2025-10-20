import pandas as pd

def detect_cloned_badges(output, place):
    df = pd.read_json(output, lines=True, encoding="utf-16")

    # groups by the user so its all the unique users and it applys the difference_between_unique_loc function
    locDiff = df.groupby("user_id").apply(lambda group: smallest_diff_between_unique_place(group, place), include_groups=False)

    locFilterNaT = locDiff[locDiff != "NaT"]
    # get users if travel times between 2 location is less than 4 hours 
    filterLoc = locFilterNaT[locFilterNaT < pd.Timedelta("4h")]

    clonedUserBadges= filterLoc.reset_index()["user_id"]

    print(clonedUserBadges)

# place has to be building_id, room_id, or location_id
def smallest_diff_between_unique_place(group, place):

    diffBetweenUniquePlace = []

    sortedValues = group.sort_values(by="timestamp").reset_index(drop=True)

    for i in range(len(sortedValues) - 1):
        # if location is the same go next because its not unique location
        if sortedValues.loc[i, place] == sortedValues.loc[i+1, place]:
            continue

        # get the difference between loc
        diff = sortedValues.loc[i+1, "timestamp"] - sortedValues.loc[i, "timestamp"]

        diffBetweenUniquePlace.append(diff)

    if not diffBetweenUniquePlace:
        return "NaT"
    else:
        return min(diffBetweenUniquePlace)
    

detect_cloned_badges(r"outputs\output4.jsonl", "location_id")