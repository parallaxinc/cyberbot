# Navigate_FLRLB.py

# Setup
#
#   If your editor has a Files feature, use it to copy all .py files from:
#	  Parallax Library (Editors with Files)
#   to your micro:bit module's file system.

from cyberbot import *

bot(22).pitch(300, 2000)

bot(18).servo_speed(120)
bot(19).servo_speed(-120)
sleep(2000)
bot(18).servo_speed(-60)
bot(19).servo_speed(-60)
sleep(1000)
bot(18).servo_speed(60)
bot(19).servo_speed(60)
sleep(2000)
bot(18).servo_speed(-60)
bot(19).servo_speed(-60)
sleep(1000)
bot(18).servo_speed(-120)
bot(19).servo_speed(120)
sleep(2000)
bot(18).servo_speed(0)
bot(19).servo_speed(0)
sleep(500)
bot(18).servo_disable()
bot(19).servo_disable()

bot().disconnect()