# count_and_pulse_in.py

# Setup
#
#   If your editor has a Files feature, use it to copy all .py files from:
#	  Parallax Library (Editors with Files)
#   to your micro:bit module's file system.

from cyberbot import *

bot(22).pitch(300, 2000)

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