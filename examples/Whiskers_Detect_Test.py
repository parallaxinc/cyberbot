# Whiskers_Detect_Test.py

from parallax import *

bot(22).frequency_out(300, 2000)

while True:
    leftWhisker = bot(7).digital_read()
    rightWhisker = bot(9).digital_read()
    
    if leftWhisker == 0:
        display.set_pixel(4, 2, 9) #right LED lights if right whisker is pressed
    else:
        display.set_pixel(4, 2, 0)
    if rightWhisker == 0:
        display.set_pixel(0, 2, 9) #left LED lights if left whisker is pressed
    else:
        display.set_pixel(0, 2, 0)