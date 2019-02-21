# Ping_Push_Pull.py

# Setup
#
#   If your editor has a Files feature, use it to copy all .py files from:
#	  Parallax Library (Editors with Files)
#   to your micro:bit module's file system.

from cyberbot import *
from ping import *
from ab360 import *

setPoint = 25
kP = -7

bot(22).pitch(300, 2000)

drive.connect()

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

    drive.speed(speed, speed)