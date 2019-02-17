# Whiskers_Roam

# Setup
#
#   If your editor has a Files feature, use it to copy all .py files from:  
#	  Parallax Library (Editors with Files) 
#   to your micro:bit module's file system.

from cyberbot import *

bot(22).pitch(300, 2000)

while True:
    left = bot(7).read_digital()
    right = bot(9).read_digital()

    if left == 1 and right == 1: #Go forward
        bot(18).servo_speed(75)
        bot(19).servo_speed(-75)
        display.show(Image.ARROW_S)
    elif left == 1 and right == 0: #Obstacle on right
        bot(18).servo_speed(-75)    #back up for 1s, turn left
        bot(19).servo_speed(75)
        display.show(Image.ARROW_N)
        sleep(1000)
        bot(18).servo_speed(-75)
        bot(19).servo_speed(-75)
        display.show(Image.ARROW_E)
        sleep(600)
    elif left == 0 and right ==1:  #Obstacle on left
        bot(18).servo_speed(-75)    #backup for 1s, turn right
        bot(19).servo_speed(75)
        display.show(Image.ARROW_N)
        sleep(1000)
        bot(18).servo_speed(75)
        bot(19).servo_speed(75)
        display.show(Image.ARROW_W)
        sleep(600)
    elif left == 0 and right == 0: #Obstacle on left + right
        bot(18).servo_speed(-75)    #backup for 1s, turn
        bot(19).servo_speed(75)
        display.show(Image.ARROW_N)
        sleep(1000)
        bot(18).servo_speed(75)
        bot(19).servo_speed(75)
        display.show(Image.ARROW_W)
        sleep(1000)