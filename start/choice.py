import os 
import pyowm
import time
import pyautogui as pg
from colorama import Fore, Back, Style
from colorama import init
init()

# Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Style: DIM, NORMAL, BRIGHT, RESET_ALL
# text overall color
print(Fore. YELLOW)
print(Style.BRIGHT)
# chain
# Run Google
print("Run Google")
time.sleep(0.1)
pg.click(802, 1063)

# Exit Google
print("Exit Google")
time.sleep(0.1)
pg.click(1899, 10)


# view
input()