from colorama import Fore, Back, Style
from colorama import init
import pyautogui as pg
import time
init()
print(pg.position())

print(Fore.GREEN)
print(Back.BLACK)
print(Style.BRIGHT)
pg.click(425, 863)
pg.typewrite("Bot connected", 0.0)
pg.typewrite(["enter"])
time.sleep(4)
pg.click(1126, 541)
pg.typewrite("w", 0.0)
pg.typewrite("w", 0.0)
pg.typewrite("w", 0.0)
pg.typewrite("w", 0.0)