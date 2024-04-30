try:
    import os, sys, time
    os.chdir(sys.argv[1])
except:
    pass

from modules.rgb import is_stage_live
import pyautogui
import cv2

RETRY = 60

for i in range(1, RETRY + 1):
    pyautogui.screenshot("./screenshots/live.png",  region=(400, 0, 1, 1))

    img = cv2.imread("./screenshots/live.png")
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    pixel = tuple(img[0, 0])

    if is_stage_live(pixel):
        print(True, f"({i}/{RETRY})")
        break

    else:
        print(False, f"({i}/{RETRY})")
        time.sleep(0.3)
        continue

# Exit
print("Enterで終了")
input()
