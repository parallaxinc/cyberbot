# Servos_Center.py

# Setup
#
#   If your editor has a Files feature, use it to copy all .py files from:  
#	  Parallax Library (Editors with Files) 
#   to your micro:bit module's file system.

from cyberbot import *

bot(22).pitch(300, 2000)

bot(18).servo_speed(0)
bot(19).servo_speed(0)

bot().disconnect()