from time import sleep

an=('|','/','-','\\')
ian = 0

while True:
    print('wait...',an[ian],sep='',end='\r')
    sleep(0.1)
    ian += 1
    if ian is len(an):ian = 0
    
