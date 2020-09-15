import pyautogui
import time

i = int(1)
delay = int(1)

while True:
    chest = pyautogui.locateOnScreen('Image\chest.png', confidence = 0.9)
    if chest != None:
        print('Clicked ' + str(i) + " time(s).")
        i += 1
        pyautogui.leftClick(chest)
        pyautogui.moveTo(700, 400)
    time.sleep(delay)