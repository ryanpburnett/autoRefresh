# DOCUMENTATION
# Keeps monitor awake.  Presses the shift key every 15 seconds (value can be changed in variable "sec"), records how many times key has been pressed.

import keyboard
import time

sec = 15
i = 0

while True:
    keyboard.press_and_release("shift")
    i = i + 1
    print("pressamundo " + str(i))
    time.sleep(sec)