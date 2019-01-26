# Terminal_Display_Up_Count.py

from parallax import *

bot(22).frequency_out(300, 2000)

counter = 0

print('hello!!!\n')

while True:
    print('counter = %d'  % counter)
    counter = counter + 1
    sleep(500)