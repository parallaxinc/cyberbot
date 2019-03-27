# QTI_Follow_Line.py

from cyberbot import *
from qti import *
from intbits import *

wL = 0
wR = 0

bot(22).tone(500, 1000)

while True:

	# Read QTI sensors
	pattern = qti(7, 4).read()

	# Display QTI sensors
	for x in range(0,4):
		z = bit.get(pattern, x)
		for y in range (0,5):
			display.set_pixel(x, y, z*9)

	# Calculate speeds to respond to detection patterns
	if pattern == 0b1000:
		wL = 10
		wR = 100

	elif pattern == 0b1100:
		wL = 30
		wR = 100

	elif pattern == 0b0100:
		wL = 60
		wR = 100

	elif pattern == 0b0110:
		wL = 100
		wR = 100

	elif pattern == 0b0010:
		wL = 100
		wR = 60

	elif pattern == 0b0011:
		wL = 100
		wR = 30

	elif pattern == 0b0001:
		wL = 100
		wR = 10

	elif pattern == 0b0000:
		bot(22).tone(500, 20)

	# Update wheel speeds
	bot(18).servo_speed(wL)
	bot(19).servo_speed(-wR)