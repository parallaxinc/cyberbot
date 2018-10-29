bot(22).frequency_out(500, 1000)

while True:

	# read the QTI sensors
	q = bot(8).qti(5)

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
	wR = 0
	wL = 0
	if q == 0b1000:
		wR = 32; wL = 16
	elif q == 0b1100:
		wR = 48; wL = 32
	elif q == 0b1110:
		wR = 64; wL = 48
	elif q == 0b0100:
		wR = 64; wL = 64
	elif q == 0b0110:
		wR = 64; wL = 64
	elif q == 0b0010:
		wR = 64; wL = 64
	elif q == 0b0111:
		wR = 48; wL = 64
	elif q == 0b0011:
		wR = 32; wL = 48
	elif q == 0b0001:
		wR = 16; wL = 32

	bot(16).servo_speed(wL)
	bot(17).servo_speed(-wR)
