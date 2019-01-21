# IR_Follow_Leader_with_DA_and_IR_Tuning.py

from parallax import *

# Correct IR sensor mismatch by increasing the dim on the side where
# the lights go out sooner as the obstacle gets closer. (0...500)
dimL     = 0
dimR     = 0

# Increase negative value for more peppy, decrease for less spastic.
kp       = -35

# Increase slower forward faster backward.  Decrease is opposite.
setPoint = 3

# Adjustments not needed.
errorL   = 0
errorR   = 0
driveL   = 0
driveR   = 0

bot(22).frequency_out(500, 1000)

while True:

    # Check obstacle distances
    irL = 0
    irR = 0
    for da in range(510, 0, -102):
        bot(20).analog_write(da + dimL)
        bot(21).analog_write(da + dimR)
        irL += bot(13).ir_detect(14, 38000)
        irR += bot(2).ir_detect(1, 38000)

    # Display obstacle distance
    display.clear()
    for n in range(0, irL, 1):
        display.set_pixel(4, n, 5)
    for n in range(0, irR, 1):
        display.set_pixel(0, n, 5)

    # Control system calculations - proportional
    errorL = setPoint - irL
    errorR = setPoint - irR
    driveL = kp * errorL
    driveR = -kp * errorR

    # Set CR servo speeds
    bot(18).servo_speed(driveL)
    bot(19).servo_speed(driveR)