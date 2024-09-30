# Clan Battle Points Tracker

## About

This is a simple script that pulls data from the **Big Games API** to track your clan's battle points. It will notify you if it thinks you caught a huge and can also play a YouTube video if you stop registering points.

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

## Setup

**User Data**  
Enter the nickname of the user(s) you want to track, their Roblox ID(s), and the clan(s) they belong to.

## Optional Configurations

- **API_URL**  
  This is pre-filled with the **Big Games API**.

- **BATTLE_TYPE**  
  Pre-filled with the current battle type.

- **UPDATE_INTERVAL_SECONDS**  
  The default update interval is set to every 5 minutes.

- **WAIT_FOR_ZERO_SECONDS**  
  Each interval will wait to update at the zero-second mark to ensure cleaner output.

- **ZERO_POINTS_THRESHOLD**  
  The number of consecutive periods with 0 points reported before triggering an alert.

- **ALERT_URL**  
  The URL to visit when a user reports 0 points over multiple consecutive intervals.

### Preview on macOS
<img width="416" alt="image" src="https://github.com/user-attachments/assets/5be2104e-1b02-451b-94dc-eced3d653e2d">

### Preview on iOS
<img width="416" alt="image" src="https://github.com/user-attachments/assets/1bf8c0d6-819b-41e0-bdbf-bf4257e4bb1f">


