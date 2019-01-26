# Ping_Push_Pull.py

from parallax import *

setPoint = 32
kP = -7

bot(22).frequency_out(300, 2000)

while True:
    distance = bot(8).ping_distance(u="cm")
    
    errorVal = setPoint - distance
    speed = kP * errorVal
    
    if speed > 0:
        display.show(Image("00000:"
            "00000:"
            "99999:"
            "09090:"
            "00900"))
    elif speed < 0:
        display.show(Image("00900:"
            "09090:"
            "99999:"
            "00000:"
            "00000"))
    else:
        display.show(Image.DIAMOND)

    bot(18).servo_speed(speed)
    bot(19).servo_speed(-speed)