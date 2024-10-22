# Made by LetsGoPikachu36 
# and RocksBlocksSocks
# 1100111 on discord

import json
import time
import webbrowser
import requests
from datetime import datetime

# Constants
API_URL = "https://biggamesapi.io/api/clan"
BATTLE_TYPE = "HalloweenBattle"
UPDATE_INTERVAL_SECONDS = 110  # Default is 2 minutes, BIG API only updates every 60 seconds
WAIT_FOR_15_SECONDS = True  # Wait for seconds to be 15 for the first update
ZERO_POINTS_THRESHOLD = 3  # Number of 0-point increases in a row before opening URL
ZERO_POINTS_URL = "https://www.youtube.com/watch?v=i77QVCt0D4U"  # URL to open when threshold is reached

# Labels and user data combined
data = {
    "labels": {
        "start": "Start",
        "time": "Time",
#        "huges": "Huges"
    },
    "users": [
        dict(name="Ash", id=1524977286, clan="fr3e", last_points=0, current_points=0, total_points_earned=0, consecutive_zeros=0),
        dict(name="Rocks", id=1328450348, clan="RFIL", last_points=0, current_points=0, total_points_earned=0, consecutive_zeros=0),
    ]
}

# Global variables
huge_suffix_count = 0  # Counter for how many times "Huge!?" was added
interval_count = 0  # Counter for how many intervals the script has run

# Helper function to calculate alignment spaces for names
def alignment_spaces(name: str, total_space: int = 8) -> str:
    return ' ' * (total_space - len(name))

# Helper function to calculate alignment spaces for current points
def alignment_spaces_for_points(current_points_str: str, max_points_length: int) -> str:
    return ' ' * (max_points_length - len(current_points_str))

def fetch_user_points(user):
    response = requests.get(f"{API_URL}/{user['clan']}")
    return response.json()  # Directly return the JSON response

def update_user_points(user, user_points):
    user["total_points_earned"] += user_points - user["last_points"]
    user["last_points"] = user["current_points"]
    user["current_points"] = user_points

def print_user_data(user, current_points_str, points_difference, max_points_length):
    spaces_name = alignment_spaces(user.get('name', 'Unknown'))
    spaces_points = alignment_spaces_for_points(current_points_str, max_points_length)
    
    if points_difference:
        print(f"{user['name']}{spaces_name}: {current_points_str}{spaces_points} ({points_difference})")
    else:
        print(f"{user['name']}{spaces_name}: {current_points_str}{spaces_points}")

def fetch_and_display_user_data():
    global huge_suffix_count
    alert = ""  # Message to display when threshold is hit

    # Determine the maximum length of formatted current points
    max_points_length = max(len(f"{user['current_points']:,}") for user in data['users'])

    for user in data['users']:
        data_from_api = fetch_user_points(user)

        # Add a 50 ms pause after each request
        time.sleep(0.05)

        if "data" in data_from_api and BATTLE_TYPE in data_from_api["data"]["Battles"]:
            battle_data = data_from_api["data"]["Battles"][BATTLE_TYPE]
            user_points = next((item["Points"] for item in battle_data["PointContributions"] if item["UserID"] == user["id"]), None)

            if user_points is None:
                print(f"User {user['name']} not found in battle {BATTLE_TYPE} for clan {user['clan']}")
                continue  # Skip to the next user

            if user["last_points"] == 0:
                user["last_points"] = user_points
                user["current_points"] = user_points
                
                # Format and display initial current points without zero padding
                current_points_str = f"{user_points:,}"
                print_user_data(user, current_points_str, "", max_points_length)
                continue
            
            # Calculate the difference and update total points earned
            update_user_points(user, user_points)

            if user["current_points"] - user["last_points"] == 0:
                user["consecutive_zeros"] += 1
            else:
                user["consecutive_zeros"] = 0

            if user["consecutive_zeros"] >= ZERO_POINTS_THRESHOLD:
                alert = f"\n{user['name']} has {ZERO_POINTS_THRESHOLD} consecutive 0-point increases!\nOpening URL...\n"
                webbrowser.open(ZERO_POINTS_URL)
                user["consecutive_zeros"] = 0
                time.sleep(60)

            points_difference = user["current_points"] - user["last_points"]
            suffix = " Great!" if points_difference > 140 else ""

            current_points_str = f"{user['current_points']:,}"
            
            if points_difference == 0:
                points_difference_str = ""
            else:
                points_difference_str = f"{points_difference:+d}{suffix}"
            
            print_user_data(user, current_points_str, points_difference_str, max_points_length)

        else:
            print(f"Battle {BATTLE_TYPE} not found!")

    if alert:
        print(alert)

try:
    # Fetch and display the user data for the first run
    print("\nFetching initial user data...\n")
    fetch_and_display_user_data()

    # Print initial timestamp
    timestamp = datetime.now().strftime("%a %m/%d %I:%M:%S %p")
    print(f"\n{data['labels']['start']}{alignment_spaces(data['labels']['start'])}: {timestamp}")

    if WAIT_FOR_15_SECONDS:
        while True:
            now = datetime.now()
            if now.second == 15:  # Wait for the 15th second of the minute
                timestamp = now.strftime("%a %m/%d %I:%M:%S %p")
                print(f"\n{data['labels']['time']}{alignment_spaces(data['labels']['time'])}: {timestamp}")
                
                fetch_and_display_user_data()
                break
            time.sleep(1)

    while True:
        if WAIT_FOR_15_SECONDS:
            while True:
                now = datetime.now()
                if now.second == 15:
                    timestamp = now.strftime("%a %m/%d %I:%M:%S %p")
                    print(f"\n{data['labels']['time']}{alignment_spaces(data['labels']['time'])}: {timestamp}")
                    break
                time.sleep(1)
        
        fetch_and_display_user_data()
        interval_count += 1
        time.sleep(UPDATE_INTERVAL_SECONDS)

except KeyboardInterrupt:
    print("\n\nStopping points tracking.\n")
    for user in data['users']:
        spaces = alignment_spaces(user['name'])
        try:
            print(f"{user['name']}{spaces}: {user['total_points_earned']:,} points gained")
        except ValueError:
            print(f"{user['name']}{spaces}: {user['total_points_earned']} points gained (unformatted)")

    print(f"\nThe script ran for {interval_count} intervals.\n")
