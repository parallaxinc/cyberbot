 # analog_write_w_qti_servos_std_cr.py

# Setup
#
#   If your editor has a Files feature, use it to copy all .py files from:
#	  Parallax Library (Editors with Files)
#   to your micro:bit module's file system.

from cyberbot import *
from qti import *

#bot(18).servo_speed(15)
#bot(19).servo_speed(-15)

#for n in range(0, 181, 10):
#	bot(17).servo_angle(n)
#	bot(16).servo_angle(9)
#	sleep(200)

#bot(17).servo_angle(0)
# bot(16).servo_angle(0)

#sleep(1000)

#bot(17).servo_angle(90)
# bot(16).servo_angle(90)

#sleep(1000)

#bot(17).servo_disable()

while True:
	bot(22).pitch(300, 1000)
	#sleep(1000)

	bot(20).write_analog(100)
	bot(21).write_analog(200)
	bot(0).write_analog(128)
	bot(5).write_analog(256)
	bot(7).write_analog(512)
	bot(15).write_analog(768)

	#bot(9).write_analog(768)
	#bot(9).write_analog(768)
	#bot(9).write_analog(768)

	sleep(1000)
	bot(0).write_analog(-1)
	bot(0).write_analog(-1)

	sleep(1000)
	bot(15).write_analog(-1)
	sleep(1000)
	bot(5).write_analog(-1)
	sleep(1000)
	bot(7).write_analog(-1)

	#bot(9).write_analog(-1)
	#bot(9).write_analog(-1)

	bot(22).pitch(300, 1500)
	sleep(1000)

	for n in range(0, 1025, 128):
		bot(15).write_analog(n)
		bot(0).write_analog(1024 - n)
		print('n=%d' %n)
		sleep(500)

	bot(22).pitch(300, 2000)
	sleep(750)

	bot(0).write_analog(-1)
	bot(5).write_analog(-1)
	bot(7).write_analog(-1)
	bot(15).write_analog(-1)
	bot(20).write_analog(-1)
	bot(21).write_analog(-1)

	sleep(1000)

	bot(0).write_analog(512)
	sleep(1000)
	bot(0).write_analog(-1)
	sleep(1000)

	bot(15).write_analog(512)
	sleep(1000)
	bot(15).write_analog(-1)
	sleep(1000)

	bot(5).write_analog(512)
	sleep(1000)
	bot(5).write_analog(-1)
	sleep(1000)

	bot(7).write_analog(512)
	sleep(1000)
	bot(7).write_analog(-1)
	sleep(1000)

	bot(22).pitch(300, 2500)
	sleep(750)

	bot(0).write_analog(128)
	bot(1).write_analog(256)
	bot(5).write_analog(512)
	bot(7).write_analog(768)

	sleep(1000)
	qti(7,7).read()

	sleep(1000)
	qti(5,0).read()

	bot(22).pitch(300, 3000)

	sleep(1000)