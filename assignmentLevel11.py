# work of Spencer Kemp
import pandas as pd

video_games_list = pd.read_csv("video_games_raw.csv")

print("Video Game Catalog Manager")

valid_row = False
# Checks if the row the user entered is valid
while valid_row == False:
    video_game_row = input("\n""Enter a row to inspect: ")
    try:
        video_game_row = int(video_game_row)
    except ValueError:
        print("Use any number inbetween 0 and 14.")
        continue

    if video_game_row >= 0 and video_game_row <= 14:
        print("\n""Selected Game:")
        print(video_games_list.iloc[video_game_row])
        valid_row = True
    else:
        print("Use any number inbetween 0 and 14.")

valid_status = False
# Checks if the status the user entered is valid
while valid_status == False:
    print("\n""Enter a new status: ")
    new_status = input("").capitalize()

    if new_status == "Backlog" or new_status == "Completed" or \
    new_status == "Playing" or new_status == "Dropped":
        video_games_list.at[video_game_row, "Status"] = new_status
        valid_status = True
    else:
        print("Invalid status. Enter playing, completed, backlog, or dropped.") #make a while loop so they can enter again
        continue
# The new recommended column
recommended_games = ["Yes", "Yes", "Yes", "No", "Yes", "Yes", "No", "No", "Yes", "No", "Yes", "Yes", "No", "Yes", "Yes"]
video_games_list["Recommended"] = recommended_games # should it be here or after so that it only shows up once

print("\n""Recommended Games:")
print(video_games_list.query("Recommended == 'Yes'")[["Title","Platform","Price","Rating"]])
# Adds to the new file and keeps the old file the same
video_games_list.to_csv("video_games_cleaned.csv", index=False)

print("The catalog has been updated.")