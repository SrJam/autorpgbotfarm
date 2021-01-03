import threading
import keyboard
import pyautogui
import time
from datetime import datetime



def hora():
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    return current_time

print("Start", hora())






def hunt():
    while True:
            time.sleep(60)

            keyboard.write('rpg hunt')
            keyboard.press_and_release('enter')
            print('huntado ', hora() + '-----------------------\n')


def recu():
    while True:
            time.sleep(304)
        

            keyboard.write('rpg net')
            keyboard.press_and_release('enter')
            print('recursos ', hora() + '-----------------------\n')

def adv():
    while True:
            time.sleep(3617)
        

            keyboard.write('rpg heal')
            keyboard.press_and_release('enter')

            keyboard.write('rpg adv')
            keyboard.press_and_release('enter')
            print('adventure ', hora() + '-----------------------\n')


def heal():
    while True:
            time.sleep(133)
        

            keyboard.write('rpg heal')
            keyboard.press_and_release('enter')
            print('curado ', hora() + '-----------------------\n')


t1 = threading.Thread(target=hunt)
t2 = threading.Thread(target=recu)
t3 = threading.Thread(target=adv)
t4 = threading.Thread(target=heal)


t1.start()
t2.start()
t3.start()
t4.start()
t1.join()
t2.join()
t3.join()
t4.join()
