# Servos_Center.py

from microbit import *
from parallax import bot

bot(22).frequency_out(500, 1000)

bot(18).servo_speed(0)
bot(19).servo_speed(0)
