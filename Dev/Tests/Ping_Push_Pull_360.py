# Ping_Push_Pull.py

from cyberbot import *
from ping import *
from feedback360 import *

setPoint = 25
kP = -7

bot(22).tone(2000, 300)

drive.connect()

while True:
	distance = ping(8).distance('cm')

	errorVal = setPoint - distance
	speed = kP * errorVal

	if speed > 0:
		display.show(Image("00000:"
			"00000:"
			"99999:"
			"09090:"
			"00900"))
	elif speed < 0:
		display.show(Image("00900:"
			"09090:"
			"99999:"
			"00000:"
			"00000"))
	else:
		display.show(Image.DIAMOND)

	drive.speed(speed, speed)