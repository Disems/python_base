import pyowm
from colorama import Fore, Back, Style
from colorama import init
init()

# Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Style: DIM, NORMAL, BRIGHT, RESET_ALL
owm = pyowm.OWM('355df60ca71ed3d954fb073d1c8cca7c' , language = "ru") 
print(Fore. YELLOW)
print("loading program...")
print("╔════════════════════════════════════╗")
print("║░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀▀░░░░║")
print("║█╗█╗████╗░████╗███╗░███╗████╗█╗░█╗█╗║")
print("║█║█║█╔══╝░█╔══╝█╔█║░█╔█║█╔══╝█║░█║█║║")
print("║███║████╗░████╗█║█║░█║█║████╗█║░█║█║║")
print("║█╔█║█╔══╝░█╔═█║█║█║░█║█║█╔══╝█║░█║╚╝║")
print("║█║█║████╗░████║███║██║█║████╗████║█╗║")
print("║╚╝╚╝╚═══╝░╚═══╝╚══╝╚═╝╚╝╚═══╝╚═══╝╚╝║")
print("╚════════════════════════════════════╝")
print(Fore. GREEN)
place = input("В каком городе/стране?: ")

observation = owm.weather_at_place(place)
w = observation.get_weather()

temp = w.get_temperature('celsius')["temp"]

print("В городе " + place + " сейчас " + w.get_detailed_status())
print("Температура сейчас в районе  " +str(temp))


if temp < 10:
    print("чел, накинь чет, холодно что пипец:З а лучше иди, и делай уроки ROFL^D")
elif temp < 20:
    print("Прохладно таки, одевайся збс...мб куртку, ок? ")
else:
    print("Температура топчик топай в футболке :ЗЗ")
print(Fore. MAGENTA)
print("")
print("░░░░░░░░░░░░░░░░░░░▄▄▄▄▄▄▄▄▄░░░░░░░░░░░░")
print("░░░░░░░░░░░░░▄▄███▀▀▀▀███████▄▄░░░░░░░░░")
print("░░░░░░░░░▄██▀██░░░░░▄██▀▀░░░░▀█▄░░░░░░░░")
print("░░░░░░░▄██░░░▀█▄▄▄██▀░░░░░░░░▀██▄░░░░░░░")
print("░░░░░░██▀██░░░░▀▀▀█▄░░░░░░░░░░░░██░░░░░░")
print("░░░░░░██░░▀██▄▄░░▄██░░░░░░░░░░░▀██▄░░░░░")
print("░░░░░██▀█▄▄░░▀▀▀██▀░░░░░░░░░░░░░░██░░░░░")
print("░░░░░██▄░▀▀█▄▄▄▄██░░░░░░░░░░░░░░▀██▄░░░░")
print("░░░░░▄███▄▄░░███▀░░░░░░░░░░░░░░░░░██░░░░")
print("░░░░░▀█▄░▀▀██▀▀░░░░░░░░░░░░░░░░░░▄█▀░░░░")
print("░░░░░░▀█████▀░░░░░░░░░░░░░░░░░░▄██▀░░░░░")
print("░░░░░▄█▀░░░░░░░░░░░░░░░░░░░░▄▄█▀▀█▄░░░░░")
print("░░░▄██░░░░░░░░░░░░░░░░░░░▄▄█▀▀░░░░██▄░░░")
print("░▄██▀▀██▄░░░░░░░░░░░▄▄▄▄█▀▀░░░░▄██▀▀██▄░")
print("█████▄▄▀▀█▄▄░░░░▄██▀▀███░░░░▄▄█▀▀▄██████")
print("████████▄░▀██▄▄▄█▀░░░░▀██▄▄██▀░▄████████")
print("███████████▄░▀██░░░░░░░░██▀░▄███████████")
print("███████████████▀░░░░░░░░▀███████████████")
print("██████████████▀░░░░░░░░░░▀██████████████")


input()


import pyautogui as pg
pg.alert("ДАААРОВА", "Взлом жопки", button="Взломаем жепку?")
age = pg.prompt("Укажите возраст: ", "Подбор очка")
print(age)
pg.confirm("Вам больше 18?", "Выбор жепки", ("Да, долбите меня полностью", "Нет, оставьте мою жепку"))
pg.password("Введите пароль от своего очка ", "Попытка пробития")




from colorama import Fore, Back, Style
from colorama import init
import pyautogui as pg
import time
init()
print(pg.position())
# Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Style: DIM, NORMAL, BRIGHT, RESET_ALL
# НАЧАЛО
# print(Fore.GREEN)
# print(Back.BLACK)
# print(Style.BRIGHT)
# pg.click(1027, 59)
# pg.typewrite("https://in-teri.ru/ucp.php?mode=login&sid=3fe5f1d84e9c385fc87393ee359be3f7", 0.0)
# pg.typewrite(["enter"])
# time.sleep(4)

# time.sleep(1)
# pg.hotkey("DOWN")
# pg.hotkey("DOWN")
# pg.hotkey("DOWN")
# pg.hotkey("DOWN")
# pg.hotkey("DOWN")
# pg.hotkey("DOWN")
# pg.hotkey("DOWN")
# pg.hotkey("DOWN")
# pg.hotkey("DOWN")
# pg.hotkey("DOWN")
# pg.hotkey("DOWN")
# pg.hotkey("DOWN")
# pg.hotkey("DOWN")
# pg.hotkey("DOWN")
# pg.hotkey("DOWN")
# pg.hotkey("DOWN")
# pg.hotkey("DOWN")
# pg.hotkey("DOWN")
# pg.hotkey("DOWN")
# pg.hotkey("DOWN")
# pg.hotkey("DOWN")
# pg.hotkey("DOWN")
# pg.hotkey("DOWN")
# pg.hotkey("DOWN")
# time.sleep(1)
# Login pg.click(1126, 541)
# Password pg.click(1144, 574)
# what0 = input(" Логин: ")
# what1 = input(" Пароль: ")


# pg.click(1126, 541)
# login = input("Имя пользователя:")
# pg.click(270, 842)
# pg.click(1126, 541)
# pg.typewrite(login, 0.0)
# password = input("Пароль:")
# pg.click(270, 842)
# pg.click(1144, 574)
# pg.typewrite(password, 0.0)
# pg.click(190, 520)
# pg.click(955, 666)
# КОНЭЦ
# ПОСЛЕ ЗАХОДА



pg.click(1027, 59)
pg.typewrite("https://in-teri.ru/posting.php?mode=reply&f=32&t=834", 0.0)
pg.typewrite(["enter"])
time.sleep(4)
pg.hotkey("DOWN")
pg.hotkey("DOWN")
pg.hotkey("DOWN")
pg.hotkey("DOWN")
pg.hotkey("DOWN")
pg.hotkey("DOWN")
pg.hotkey("DOWN")
pg.hotkey("DOWN")
pg.hotkey("DOWN")
pg.hotkey("DOWN")
pg.hotkey("DOWN")
pg.hotkey("DOWN")
pg.hotkey("DOWN")
pg.hotkey("DOWN")
pg.hotkey("DOWN")
pg.hotkey("DOWN")
pg.hotkey("DOWN")
time.sleep(1)
pg.click(877, 771)

