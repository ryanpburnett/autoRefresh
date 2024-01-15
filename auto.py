# DOCUMENTATION
# While the 'p' key is held down, ctrl+r will be hit every 15 seconds, refreshing any webpage that is open.  
# These variables can be modified as needed.
# A counter will keep track of 'refresh' time and 'pause' time.

#issue with ctrl+r not working, is it refresing constantly? figure out underlying issue

import keyboard
import time
from datetime import timedelta

sec = 15
refresh = 0
pause = 0

print("----------------")

while True:
    if keyboard.is_pressed("p"):
        keyboard.press_and_release("ctrl+r")
        refresh += sec
    else: 
        pause += sec

    print("refresh\t", timedelta(seconds=refresh))
    print("pause\t", timedelta(seconds=pause))
    print("----------------")
    time.sleep(sec)