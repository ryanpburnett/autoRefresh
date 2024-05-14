# DOCUMENTATION
# While the 'p' key is held down, ctrl+r will be hit every 15 seconds, refreshing any webpage that is open.  
# These variables can be modified as needed.
# A counter will keep track of 'refresh' time and 'pause' time.

#issue with ctrl+r not working, is it refresing constantly? figure out underlying issue

import keyboard
import time

sec = 15
i = 0

while True:
    keyboard.press_and_release("shift")
    i = i + 1
    print("pressamundo " + str(i))
    time.sleep(sec)