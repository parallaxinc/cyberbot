# Terminal_Display_Up_Count.py

from cyberbot import *

bot(22).pitch(300, 2000)

counter = 0

print('hello!!!\n')

while True:
	print('counter = %d'  % counter)
	counter = counter + 1
	sleep(500)