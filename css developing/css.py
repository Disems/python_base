import pyowm
from colorama import Fore, Back, Style
from colorama import init
import pyautogui as pg
import time
init()

# Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Style: DIM, NORMAL, BRIGHT, RESET_ALL
print(Fore. GREEN)
print(Style.BRIGHT)
pg.click(234, 59)
pg.typewrite("https://in-teri.ru/posting.php?mode=reply&f=32&t=834", 0.0)
pg.typewrite(["enter"])
time.sleep(4)