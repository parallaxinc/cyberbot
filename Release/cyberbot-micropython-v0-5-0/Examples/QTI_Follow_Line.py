# QTI_Follow_Line.py

from cyberbot import *
from qti import *

wL = 0
wR = 0

bot(22).pitch(300, 2000)

while True:

	# read the QTI sensors  bot(end pin).qti(start pin)
	q = qti(7,4).read()

	# bin = "{0:b}".format(q)
	# print('q = %s' % bin)
	# sleep(1000)

	# show the line sensors on the display
	mask = [1, 2, 4, 8]
	for x in range(0,4):
		z = 0
		if (q & mask[x]) != 0:
			z = 9
		for y in range(0,4):
			display.set_pixel(x, y, z)

	# set the wheel speed variables according
	# to the QTI sensor output
	if q == 0b1000:
		wR = 32
		wL = -16
	elif q == 0b1100:
		wR = 32
		wL = 16
	elif q == 0b1110:
		wR = 64
		wL = 32
	elif q == 0b0100:
		wR = 64
		wL = 64
	elif q == 0b0110:
		wR = 64
		wL = 64
	elif q == 0b0010:
		wR = 64
		wL = 64
	elif q == 0b0111:
		wR = 32
		wL = 64
	elif q == 0b0011:
		wR = 16
		wL = 32
	elif q == 0b0001:
		wR = -16
		wL = 32
	elif q == 0b0000:
		wR = 32
		wL = -32

	bot(18).servo_speed(wL)
	bot(19).servo_speed(-wR)