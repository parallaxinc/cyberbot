# Navigate_FLRLB.py

from cyberbot import *

bot(22).tone(2000, 300)

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
sleep(500)
bot(18).servo_disable()
bot(19).servo_disable()

bot().detach()