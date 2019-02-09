# IR_Roam_Avoid_Obstacles.py

# Setup
#
#   If your editor has a Files feature, use it to copy all .py files from:  
#	  Parallax Library (Editors with Files) 
#   to your micro:bit module's file system.

from cyberbot import *

bot(22).pitch(300, 2000)

while True:

    # Pin in the reciever, detect is the IR LED
    irL = bot(13).ir_detect(14, 37500)
    irR = bot(2).ir_detect(1, 37500)

    bot(20).write_digital(irL)
    bot(21).write_digital(irR)

    if irL == 1 and irR == 1:
        bot(18).servo_speed(64)
        bot(19).servo_speed(-64)
        display.show(Image.HAPPY)
    elif irL == 0 and irR == 0:
        bot(18).servo_speed(-64)
        bot(19).servo_speed(64)
        display.show(Image.SAD)
    elif irL == 0:
        bot(18).servo_speed(64)
        bot(19).servo_speed(64)
        display.show(Image.SAD)
    elif irR == 0:
        bot(18).servo_speed(-64)
        bot(19).servo_speed(-64)
        display.show(Image.SAD)