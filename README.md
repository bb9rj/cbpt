# Clan Battle Points Tracker

## About

This is a simple script that pulls data from the Big Games API to track your clan battle points. It will call out a period as 'Great' if you score over 70 ppm.

## Setup

**User Data**  
Enter the nickname of the user(s) you want to track, their Roblox ID(s), and the clan(s) they belong to.

## Running the Script

### macOS

1. Open Terminal.
2. Type `python3`.
3. Drag the script file into your terminal window.
4. Press `Enter`.

### Windows

1. Open the Command Prompt.
2. Type `python`.
3. Either `cd` to the directory of the script or provide the full path to the script file including the filename.
4. Press `Enter`.

**To stop the script:**  
Press `Ctrl + C`.

### iOS

1. Use an app like **Pyto** to run the script.

## Optional Configurations

- **API_URL**  
  This is pre-filled with the **Big Games API**.

- **BATTLE_TYPE**  
  Pre-filled with the current battle type.

- **UPDATE_INTERVAL_SECONDS**  
  The default update interval is set to every 5 minutes on desktop, and 2 minutes on mobile.

- **WAIT_FOR_ZERO_SECONDS**  
  Each interval will wait to update at the zero-second mark to ensure cleaner output.

- **ZERO_POINTS_THRESHOLD**  
  The number of consecutive periods with 0 points reported before triggering an alert.

- **ALERT_URL**  
  The URL to visit when a user reports 0 points over multiple consecutive intervals.

### Previews
<img width="300" alt="image" src="https://github.com/user-attachments/assets/fbeea6f2-5aee-4590-9381-3ccfe174779c">

## Download
Halloween battle version: [https://github.com/bb9rj/cbpt/blob/main/points_checker_20.py]

