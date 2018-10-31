##################################
# Whisker Test                   #
##################################

while True:
    leftWhisker = bot(6).digital_read()
    rightWhisker = bot(8).digital_read()
    
    if leftWhisker == 0:
        display.set_pixel(0, 2, 9)
    else:
        display.set_pixel(0, 2, 0)
    if rightWhisker == 0:
        display.set_pixel(4, 2, 9)
    else:
        display.set_pixel(4, 2, 0)
