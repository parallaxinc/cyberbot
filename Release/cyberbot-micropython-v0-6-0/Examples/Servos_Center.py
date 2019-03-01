# Servos_Center.py

from cyberbot import *

bot(22).tone(2000, 300)

bot(18).servo_speed(0)
bot(19).servo_speed(0)

bot().detach()