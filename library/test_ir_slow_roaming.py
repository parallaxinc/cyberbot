###############################
# IR Detection - Slow Roaming #
###############################

bot_pin(22).frequency_out(500, 1000)
 
while True:

    # Detect is the IR LED, pin is receiver
    irR = bot_pin(3).ir_detect(1, 37500)
    irL = bot_pin(9).ir_detect(11, 35700)
    
    bot_pin(21).digital_write(irR)
    bot_pin(20).digital_write(irL)
    
    if irL == 1 and irR == 1:
        bot_pin(18).servo_speed(32)
        bot_pin(19).servo_speed(-37)
        display.show(Image.HAPPY)
    elif irL == 0 and irR == 0:
        bot_pin(18).servo_speed(-32)
        bot_pin(19).servo_speed(32)
        display.show(Image.SAD)
    elif irL == 0:
        bot_pin(18).servo_speed(32)
        bot_pin(19).servo_speed(32)
        display.show(Image.SAD)
    elif irR == 0:
        bot_pin(18).servo_speed(-32)
        bot_pin(19).servo_speed(-32)
        display.show(Image.SAD)
