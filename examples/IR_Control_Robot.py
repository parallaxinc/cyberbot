##################################
# IR Control Robot               #
# IR detector connected to pin 0 #
##################################

while True:
    num = bot(0).tv_remote()
    
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
        
