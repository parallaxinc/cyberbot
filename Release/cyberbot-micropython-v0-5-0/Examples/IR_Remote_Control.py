##################################
# IR_Remote_Control.py           #
# IR detector connected to pin 2 #
##################################

# Setup
#
#   If your editor has a Files feature, use it to copy all .py files from:
#	  Parallax Library (Editors with Files)
#   to your micro:bit module's file system.

from cyberbot import *
from tv_remote import *

bot(22).pitch(300, 2000)

while True:
    num = ir(2).remote()

    if num == 2:
        bot(18).servo_speed(75)
        bot(19).servo_speed(-75)
        display.show(Image.ARROW_S)
    elif num == 4:
        bot(18).servo_speed(-75)
        bot(19).servo_speed(-75)
        display.show(Image.ARROW_E)
    elif num == 5:
        bot(18).servo_speed(0)
        bot(19).servo_speed(0)
        display.show(Image.HAPPY)
    elif num == 6:
        bot(18).servo_speed(75)
        bot(19).servo_speed(75)
        display.show(Image.ARROW_W)
    elif num == 8:
        bot(18).servo_speed(-75)
        bot(19).servo_speed(75)
        display.show(Image.ARROW_N)