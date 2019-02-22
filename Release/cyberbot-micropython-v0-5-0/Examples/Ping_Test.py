# Ping_Test.py

from cyberbot import *
from ping import *

bot(22).pitch(300, 2000)

while True:
	distance = ping(8).distance(u="cm")
	print('dist = %d' % distance)
	display.scroll(str(distance), 125)
	sleep(750)