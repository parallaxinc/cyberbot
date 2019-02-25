# Ping_Test.py

from cyberbot import *
from ping import *

bot(22).tone(2000, 300)

while True:
	distance = ping(8).distance()
	print('Dist() = %d' % distance)
	distance = ping(8).distance('cm')
	print('Dist(cm) = %d' % distance)
	distance = ping(8).distance('in')
	print('Dist(in) = %d' % distance)
	distance = ping(8).distance('us')
	print('Dist(us) = %d\r' % distance)
	#display.scroll(str(distance), 125)
	sleep(750)