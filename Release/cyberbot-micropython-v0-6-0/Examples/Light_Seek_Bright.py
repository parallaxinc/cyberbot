# Light_Seek_Bright.py

from cyberbot import *

bot(22).tone(2000, 300)

while True:

	# Read the phototransistors, qt stands for charge time
	#bot(5).write_digital(1)
	#bot(11).write_digital(1)
	qtR = bot(5).rc_time(1)
	qtL = bot(11).rc_time(1)

	# Make one normalized differential measurement
	# from R/L sensor measurements.
	nDiff = (200 * qtR) / (qtR + qtL + 1) - 100

	# Optionally scale nDiff for sharper turn responses.
	nDiff = (nDiff * 4) / 2

	# print("qtL = %d, qtR = %d, nDiff = %d" % (qtL, qtR, nDiff))
	# sleep(1000)

	# Set wheel speeds according to nDiff
	# Omega looks like a lower-case w and is used in rotational
	# velocity calculations.
	if nDiff > 0:
		wL = 64 - nDiff
		wR = -64
	else:
		wL = 64
		wR = -64 - nDiff

	bot(18).servo_speed(wL)
	bot(19).servo_speed(wR)