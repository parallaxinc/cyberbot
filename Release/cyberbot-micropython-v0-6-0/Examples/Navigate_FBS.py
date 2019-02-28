# Navigate_FBS.py

from cyberbot import *

bot(22).tone(2000, 300)

bot(18).servo_speed(120)
bot(19).servo_speed(-120)
sleep(700)
bot(18).servo_speed(-120)
bot(19).servo_speed(120)
sleep(700)
bot(18).servo_speed(0)
bot(19).servo_speed(0)
sleep(1000)
bot(18).servo_speed()
bot(19).servo_speed()
bot().detach()