# RC_Decay_Pos_Neg.py

# Setup
#
#   If your editor has a Files feature, use it to copy all .py files from:
#	  Parallax Library (Editors with Files)
#   to your micro:bit module's file system.

from cyberbot import *

bot(22).pitch(300, 2000)

while True:

	# Test with IO---220---(photoQ || C)---GND

	# Charge to 3/4 of 3.3 V for 2 ms
	qtR = bot(5).rc_time(1,2000,768)
	qtL = bot(8).rc_time(1,2000,768)

	# Charge to 3.3 V for 2 ms
	#qtR = bot(5).rc_time(1,2000)
	#qtL = bot(8).rc_time(1,2000)

	# Charge to 3.3 V for 1 ms
	#qtR = bot(5).rc_time(1)
	#qtL = bot(8).rc_time(1)


	# Test with IO---220---(potR || C)---5 V

	# Charge to 1/4 of 3.3. V for 2 ms
	#qtR = bot(5).rc_time(0,2000,256)
	#qtL = bot(8).rc_time(0,2000,256)

	# Charge to 0 V for 2 ms
	#qtR = bot(5).rc_time(0,2000)
	#qtL = bot(8).rc_time(0,2000)

	# Charge to 0 V for 1 ms
	#qtR = bot(5).rc_time(0)
	#qtL = bot(8).rc_time(0)

	print("qtL = %d, qtR = %d" % (qtL, qtR))
	sleep(750)