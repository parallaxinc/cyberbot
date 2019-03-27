# Display_QTI_Detections.py
# Test program uses micro:bit LEDs to display QTI states

from cyberbot import *					# import modules
from qti import *
from intbits import *

bot(22).tone(500, 1000)					# start beep

while True:								# main loop

	pattern = qti(7, 4).read()			# store 1/0 detect states in pattern

	for x in range(0,4):				# loop 4x count LED columns with x
		z = bit.get(pattern, x)			# get 1s or 0s from pattern
		for y in range (0,5):			# use y to visit each row
			display.set_pixel(x, y, z*9)# LED on 9 or off 0 in x-col y-row