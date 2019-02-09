# Ping_Push_Pull.py

# Setup
#
#   o  Open cyberbot.py from: 
#	     Parallax Library (Editors without Files)
#   o  Copy all of it and paste over from cyberbot import * 
#	o  Open ping.py from the same folder and paste it over from ping import *

from cyberbot import *
from ping import *

setPoint = 32
kP = -7

bot(22).pitch(300, 2000)

while True:
    distance = ping(8).distance(u="cm")

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