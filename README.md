# Autojoin-zoom-meetings

The auto-zoom meeting joiner helps you to join scheduled zooms in your absence so you dont miss out on important meeting and also reduces the work of having to join the meeting yourself (The power of automation ^_^ ).

# Downloading and installing python modules

For windows, use command prompt and for linux users, use in-built terminal and run the below mentioned commands -

      "pip install pyautogui"

      "pip install click"
      
# Setting up cursor

To setup cursor, use the set_cursor.py file. 

1. Firstly, place the cursor on "Open zoom meetings" in browser and run the set_cursor.py file to get the co-ordinates and replace it in line 25 in the main file.
2. After opening the meeting, you can choose to either join the audio or not join the audio, so depending on your choice, place the cursor in either "join audio" or "close" options and run the set_cursor.py file to get the co-ordinates and update them in autozoom.py

Once your done with setting up your cursor, schedule your zoom meetings as mentioned in autozoom.py and your good to go. ^^
