# Whiskers_Detect_Test.py

# Setup
#
#   If your editor has a Files feature, use it to copy all .py files from:  
#	  Parallax Library (Editors with Files) 
#   to your micro:bit module's file system.

from cyberbot import *

bot(22).pitch(300, 2000)

while True:
    leftWhisker = bot(7).read_digital()
    rightWhisker = bot(9).read_digital()
    
    if leftWhisker == 0:
        display.set_pixel(4, 2, 9) #right LED lights if right whisker is pressed
    else:
        display.set_pixel(4, 2, 0)
    if rightWhisker == 0:
        display.set_pixel(0, 2, 9) #left LED lights if left whisker is pressed
    else:
        display.set_pixel(0, 2, 0)