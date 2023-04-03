# import keyboard
# import time
# from datetime import timedelta

# sec = 15
# refresh = 0
# pause = 0

# while True:
#     if keyboard.is_pressed("p"):
#         keyboard.press_and_release("ctrl+r")
#         print("refresh\t", timedelta(seconds=refresh))
#         refresh += sec
#     else: 
#         print("pause\t", timedelta(seconds=pause))
#         pause += sec

#     time.sleep(sec)

# ----ALTERNATE VERSION----

import keyboard
import time
from datetime import timedelta

sec = 15
refresh = 0
pause = 0

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