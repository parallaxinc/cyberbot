# WORK IN PROGRESS

bot(22).frequency_out(500, 1000)

while True:

	# read the phototransistors
	pL = bot(9).rc_time(1)
	pR = bot(5).rc_time(1)

	# show the phototransistors sensors on the display
	# creates a log-scaled bar graph
	gL = trunc(log(pL, 10)) + 1
	gR = trunc(log(pR, 10)) + 1
	for y in range(0,4):
		if y <= gL:
			display.set_pixel(4, y, 9)
		else:
			display.set_pixel(4, y, 0)
		if y <= gR:
			display.set_pixel(0, y, 9)
		else:
			display.set_pixel(0, y, 0)

	# calculate the normalized differential of the measurements
	nDiff = trunc((200 * pR) / (pR + pL) - 100)

	# set the wheel speed variables according
	# to the normalized differential
	wR = 64
	wL = 64
	if nDiff > 0:
		wL = 64 - nDiff
	else:
		wR = 64 + nDiff

	bot(16).servo_speed(wL)
	bot(17).servo_speed(-wR)
