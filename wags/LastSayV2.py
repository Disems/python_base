import pyautogui as pg

# pg.move(500, 50, 1.5)

# print(pg.position())

# pg.click(785, 56)
# pg.typewrite("https://pyautogui.readthedocs.io/en/latest/mouse.html")
# pg.typewrite(["enter"])
# pg.click(22, 20)
# pg.hotkey("winleft")
# pg.typewrite("chrome", 0,5)
# pg.typewrite(["enter"])
# pg.typewrite("https://vk.com/im\n", 0.2)
# pg.typewrite(["enter"])

pg.alert("Some", "Title Message", button="Button text")
age = pg.prompt("Enter Your Age", "Your age")
print(age)
pg.confirm("you are older than 18+" "are you sure?", ("yes, older", "noo"))
pg.password("Enter password", "Password title")