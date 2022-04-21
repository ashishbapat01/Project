import random
import pyautogui as pg
import time

name =  ('S','H','C','G','I')
time.sleep(10)

for i in range (5):
    a = random.choice(name)
    pg.write(' The is  '+a)
    pg.press('enter')




