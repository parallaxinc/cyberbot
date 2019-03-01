# count_and_pulse_in.py

from cyberbot import *

bot(22).tone(2000, 300)

while True:

	#bot(0).servo_speed(0)
	bot(0).servo_speed(100)
	# bot(0).write_digital(1)
	# bot(0).write_digital(0)

	while True:
		f = bot(0).pulse_count(1000)
		tH = bot(0).pulse_in(1)
		tL = bot(0).pulse_in(0)
		print("f = %d, th = %d, tL = %d" % (f, tH, tL))
		sleep(750)