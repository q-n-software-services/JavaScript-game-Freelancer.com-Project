import time
import keyboard
import pyautogui as pt
import pyperclip

fhand = open('Tareekh ke Auraq.txt')
fhand = fhand.readlines()

time.sleep(5)
i = 1
for link in fhand:
    if len(link.strip()) > 12:
        url = link.split()[1].strip()
        if len(url) > 5:
            pyperclip.copy(url)
            pt.moveTo(542, 53)
            pt.click()
            keyboard.write(url)
            keyboard.press('enter')

            time.sleep(5)

            pt.moveTo(583, 658)
            pt.click()
            time.sleep(1)

            pt.moveTo(584, 685)
            pt.click()
            time.sleep(1)




            print(i)
            i += 1


