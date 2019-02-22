# Servos_Center.py

from cyberbot import *

bot(22).pitch(300, 2000)

bot(18).servo_speed(0)
bot(19).servo_speed(0)

bot().disconnect()