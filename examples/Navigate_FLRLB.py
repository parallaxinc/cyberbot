# Navigate_FLRLB.py

from parallax import *

bot(22).frequency_out(300, 2000)

bot(18).servo_speed(120)
bot(19).servo_speed(-120)
sleep(2000)
bot(18).servo_speed(-60)
bot(19).servo_speed(-60)
sleep(1000)
bot(18).servo_speed(60)
bot(19).servo_speed(60)
sleep(2000)
bot(18).servo_speed(-60)
bot(19).servo_speed(-60)
sleep(1000)
bot(18).servo_speed(-120)
bot(19).servo_speed(120)
sleep(2000)
bot(18).servo_speed(0)
bot(19).servo_speed(0)

bot().disconnect()