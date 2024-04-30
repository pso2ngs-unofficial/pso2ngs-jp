try:
    import os, sys, time
    os.chdir(sys.argv[1])
except:
    pass

from modules.pso2ngs import HALPHA, FAILED, NODATA, is_incomplete, is_all_nodata
from modules.rgb import is_urgent_quest
import pyautogui
import cv2

RETRY = 60

for i in range(1, RETRY + 1):
    pyautogui.screenshot("./screenshots/quest.png", region=(0, 0, 256, 256))

    img = cv2.imread("./screenshots/quest.png")
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    determined = []

    for region in HALPHA:
        found = []

        for quest in region:
            quest_name, quest_coordinate = quest
            left, top = quest_coordinate
            pixel = tuple(img[top, left])

            if is_urgent_quest(pixel):
                found.append(quest_name)

        if len(found) == 1:
            determined.append(found[0])
        else:
            if len(found) > 1:
                determined.append(FAILED)
            else:
                determined.append(NODATA)

    if is_incomplete(determined) and (i) != RETRY:
        print(False, f"({i}/{RETRY})")
        time.sleep(0.3)
        continue

    elif is_all_nodata(determined):
        print(False, f"({i}/{RETRY})")
        break

    else:
        print(True, f"({i}/{RETRY})")
        print(determined)
        break

# Exit
print("Enterで終了")
input()
