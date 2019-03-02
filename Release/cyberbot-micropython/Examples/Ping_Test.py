# Ping_Test.py

from cyberbot import *
from ping import *

bot(22).tone(2000, 300)

while True:
	distance = ping(8).distance('cm')
	print('dist = %d' % distance)
	display.scroll(str(distance), 125)
	sleep(750)