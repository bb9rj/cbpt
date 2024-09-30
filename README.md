#Clan battle points tracker

# About
This is a simple script that pulls data from the Big Games API to track your clan battle points, it will note if it thinks you got a huge, and play a youtube video if you stop registering points.



# Running the script

To run on MacOS 
1. Open the terminal
2. Type 'python3'
3. Drag the file to your terminal window
4. Press enter

To run on Windows 
1. Open the command line
2. Type 'python'
3. Either cd or write the path to the file along with the file name
4. Press enter

Hit control C to stop

To run on iOS
1. Use an app like Pyto



# Setup

User data

Enter the nickname of the user(s) you want to track, their roblox id(s), and the clan(s) they belong to



# Optional

API_URL

This is prefilled with the Big Games API

BATTLE_TYPE

Prefilled with current battle

UPDATE_INTERVAL_SECONDS

Default setup is every 5 minutes

WAIT_FOR_ZERO_SECONDS

Each interval will wait to update when the seconds are 0 so it looks cleaner

ZERO_POINTS_THRESHOLD

How many period of 0 points reported before running the alert

ZERO_POINTS_THRESHOLD

The url to go to if the user has reported multiple consecutive intervals of 0 points

