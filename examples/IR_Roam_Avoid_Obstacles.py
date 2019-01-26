# IR_Roam_Avoid_Obstacles.py

from parallax import *

bot(22).frequency_out(300, 2000)

while True:

    # Pin in the reciever, detect is the IR LED
    irL = bot(13).ir_detect(14, 37500)
    irR = bot(2).ir_detect(1, 37500)

    bot(20).digital_write(irL)
    bot(21).digital_write(irR)

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