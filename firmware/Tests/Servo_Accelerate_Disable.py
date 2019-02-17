# Navigate_FBS.py

from cyberbot import *

bot(22).pitch(300, 2000)

# bot(18).servo_speed(1)

bot(18).servo_accelerate(1)
bot(19).servo_accelerate(2)
sleep(2000)

bot(18).servo_speed(100)
bot(19).servo_speed(-100)
sleep(5000)
bot(18).servo_speed(0)
bot(19).servo_speed(0)
sleep(2000)
bot(18).servo_speed(100)
bot(19).servo_speed(-100)
sleep(5000)
bot(18).servo_disable()
bot(19).servo_disable()

# x = 0
# while True:
#     x = x + 1

bot().disconnect()