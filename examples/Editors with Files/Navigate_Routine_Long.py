##############################################
# Navitate_Routine_Long                      #
# Long Navigation Routine - MEMORY MAXED OUT #
# Requires v0.3                              #
##############################################

# Setup
#
#   If your editor has a Files feature, use it to copy all .py files from:
#	  Parallax Library (Editors with Files)
#   to your micro:bit module's file system.

from cyberbot import *

bot(22).pitch(300, 2000)

# 96 if you leave it connected.
# directions = 'FBLRSLRFLRSFBLRSLRFLRSFBLRSLRFLRSFBLRSLRFLRSFBLRSLRFLRSFBLRSLRFLRSFBLRSLRFLRSFBLRSLRFLRSFBLRSLRF'
# durations =  [3,2,.5,.5,1.5,.5,1,.5,.5,.5,3,3,2,.5,.5,1.5,.5,1,.5,.5,.5,3,3,2,.5,.5,1.5,.5,1,.5,.5,.5,3,3,2,.5,.5,1.5,.5,1,.5,.5,.5,3,3,2,.5,.5,1.5,.5,1,.5,.5,.5,3,3,2,.5,.5,1.5,.5,1,.5,.5,.5,3,3,2,.5,.5,1.5,.5,1,.5,.5,.5,3,3,2,.5,.5,1.5,.5,1,.5,.5,.5,3,3,2,.5,.5,1.5,.5,1,.5,.5,.5]

# 145 if you disconnect and restart.
directions = 'FBLRSLRFLRSFBLRSLRFLRSFBLRSLRFLRSFBLRSLRFLRSFBLRSLRFLRSFBLRSLRFLRSFBLRSLRFLRSFBLRSLRFLRSFBLRSLRFBLRSLRFLRSFBLRSLRFBLRSLRFLRSFBLRSLRFBLRSLRFLRSFBL'
durations =  [3,2,.5,.5,1.5,.5,1,.5,.5,.5,3,3,2,.5,.5,1.5,.5,1,.5,.5,.5,3,3,2,.5,.5,1.5,.5,1,.5,.5,.5,3,3,2,.5,.5,1.5,.5,1,.5,.5,.5,3,3,2,.5,.5,1.5,.5,1,.5,.5,.5,3,3,2,.5,.5,1.5,.5,1,.5,.5,.5,3,3,2,.5,.5,1.5,.5,1,.5,.5,.5,3,3,2,.5,.5,1.5,.5,1,.5,.5,.5,3,3,2,.5,.5,1.5,.5,1,.5,.5,.5,.5,1.5,.5,1,.5,.5,.5,3,3,2,.5,.5,1.5,.5,1,.5,.5,.5,.5,1.5,.5,1,.5,.5,.5,3,3,2,.5,.5,1.5]

for direction, duration in zip(directions, durations):
    if direction == 'F':
        display.show(Image.ARROW_S)
        bot(18).servo_speed(50, -50)
    elif direction == 'B':
        display.show(Image.ARROW_N)
        bot(18).servo_speed(-50, 50)
    elif direction == 'R':
        display.show(Image.ARROW_W)
        bot(18).servo_speed(50, 50)
    elif direction == 'L':
        display.show(Image.ARROW_E)
        bot(18).servo_speed(-50, -50)
    else:
        display.show(Image.SQUARE_SMALL)
        bot(18).servo_disable()
        bot(19).servo_disable()

    sleep(duration * 1000)

display.clear
bot(18).servo_disable()
bot(19).servo_disable()

bot(22).pitch(500, 2000)

bot().disconnect()