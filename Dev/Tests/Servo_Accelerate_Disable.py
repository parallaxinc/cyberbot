# Navigate_FBS.py

from cyberbot import *

bot(22).tone(2000, 300)

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
sleep(8000)
#bot(18).servo_speed(None)
#bot(19).servo_speed(None)
#sleep(2000)
bot(18,19).servo_speed(-100,100)
sleep(5000)
bot(18).servo_speed(20)
sleep(5000)
bot(19).servo_speed(-20)
sleep(2000)
bot(18).servo_speed()
bot(20).write_digital(1)
sleep(2000)
bot(19).servo_speed(None)
bot(21).write_digital(1)
sleep(3000)
#leave bot moving slowly
#bot(18,19).servo_speed(-10,10)
#sleep(2000)
bot(18,19).servo_speed(100,-100)
bot(20).write_digital(0)
bot(21).write_digital(0)
sleep(3000)
bot(18).servo_speed()
bot(20).write_digital(1)
sleep(2000)
bot(19).servo_speed(None)
bot(21).write_digital(1)
sleep(3000)

bot().detach()