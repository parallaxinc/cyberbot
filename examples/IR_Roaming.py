##########################
# IR Roaming             #
##########################

bot(22).frequency_out(500, 1000)
 
while True:
    
    # Pin in the reciever, detect is the IR LED
    irR = bot(3).ir_detect(1, 37500)
    irL = bot(9).ir_detect(11, 37500)
    
    bot(21).digital_write(irR)
    bot(20).digital_write(irL)
    
    if irL == 1 and irR == 1:
        bot(18).servo_speed(32)
        bot(19).servo_speed(-37)
        display.show(Image.HAPPY)
    elif irL == 0 and irR == 0:
        bot(18).servo_speed(-32)
        bot(19).servo_speed(32)
        display.show(Image.SAD)
    elif irL == 0:
        bot(18).servo_speed(32)
        bot(19).servo_speed(32)
        display.show(Image.SAD)
    elif irR == 0:
        bot(18).servo_speed(-32)
        bot(19).servo_speed(-32)
        display.show(Image.SAD)
