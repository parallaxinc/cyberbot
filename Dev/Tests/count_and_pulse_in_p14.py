# count_and_pulse_in.py

from cyberbot import *

bot(22).tone(2000, 300)

while True:

	#bot(15).servo_speed(0)
	bot(15).servo_speed(100)
	# bot(15).write_digital(1)
	# bot(15).write_digital(0)

	while True:
		f = bot(15).pulse_count(1000)
		tH = bot(15).pulse_in(1)
		tL = bot(15).pulse_in(0)
		print("f = %d, th = %d, tL = %d" % (f, tH, tL))
		sleep(750)