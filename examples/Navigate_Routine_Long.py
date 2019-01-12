##############################################
# Navitate_Routine_Long                      #
# Long Navigation Routine - MEMORY MAXED OUT #
# Requires v0.3                              #
##############################################

from parallax import *

bot(22).frequency_out(500, 1000)

directions = 'LRFLRSFBLRSBFBLRSFBLRSBFFBLRSFBLRSB'
durations =  [.5,.5,1,.5,.5,3,3,2,.5,.5,1,2,3,1,.5,.5,3,3,2,.5,.5,1,2,3,1,2,.5,.5,3,3,2,.5,.5,1,2]

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

bot(22).frequency_out(500, 2000)