###### 1 ######

# int
# name1 = 3
# age = 15
# float
# fnumber = 5.7
# str
# name = "Dima"
# print("Привет, меня зовут " + name + "!")
# print("Мне " + str(age) + " age!")

###### 2 ######

# name = input("Введите свое имя:")
# age = input("Сколько тебе лет:")

#print("Hello, " + name + "!")
#print("Тебе уже " + age + " это круто!")

###### 3 ######
# Калькулятор #
from colorama import Fore, Back, Style
from colorama import init
init()

# Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Style: DIM, NORMAL, BRIGHT, RESET_ALL
print(Fore.GREEN)
print(Back.BLACK)
print(Style.BRIGHT)
what = input(" Что делаем? (+,-): ")

a = input("one change:")
b = input("two change:")

if what == "+":
    c = a + b
    print("Result" + c)    
elif what == "-":
    c = a - b
    print("Result: " + str(c) +)
else:
    print("Error")
input()



import pyautogui as pg
import time
print(pg.position())
# pg.click(733, 951)
# css pg.click(231, 865)
# pg.click(231, 865)
# pg.leftclick(515, 227)
# pg.typewrite("/admins", 0.0)
# pg.typewrite(["enter"])

# GS
# pg.click(1169, 1000)
# time.sleep(5)
# pg.click(1169, 1000)

# google
pg.click(565, 23)
# input line
pg.click(843, 57)
pg.typewrite("https://vk.com/audios435909507", 0.0)
pg.typewrite(["enter"])
time.sleep(4)
pg.click(732, 630)
time.sleep(2)
pg.click(1256, 162)
time.sleep(1)
pg.click(1004, 99)





['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(',
')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
'8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~',
'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
'browserback', 'browserfavorites', 'browserforward', 'browserhome',
'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',
'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',
'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',
'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',
'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
'command', 'option', 'optionleft', 'optionright']