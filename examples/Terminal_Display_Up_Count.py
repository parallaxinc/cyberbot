# Terminal_Display_Up_Count.py

from microbit import *

counter = 0

print('hello!!!\n')

while True:
    print('counter = %d'  % counter)
    counter = counter + 1
    sleep(500)