# Servos_Center.py

# Setup
#
#   o  Open cyberbot.py from: 
#	     Parallax Library (Editors without Files)
#   o  Copy all of it and paste over from cyberbot import * 

from cyberbot import *

bot(22).pitch(300, 2000)

bot(18).servo_speed(0)
bot(19).servo_speed(0)

bot().disconnect()