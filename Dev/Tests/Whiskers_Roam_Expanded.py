# Whiskers_Roam_Expanded.py

from cyberbot import *

bot(22).pitch(300, 2000)

while True:
	left = bot(7).read_digital()
	right = bot(9).read_digital()

	if left == 1 and right == 1: #Go forward
		bot(18).servo_speed(75)
		bot(19).servo_speed(-75)
		display.show(Image.ARROW_S)
		bot(15).write_digital(0)
		bot(0).write_digital(0)
	elif left == 1 and right == 0: #Obstacle on right
		bot(18).servo_speed(-75)	#back up for 1s, turn left
		bot(19).servo_speed(75)
		display.show(Image.ARROW_N)
		bot(15).write_digital(0)
		bot(0).write_digital(1)
		sleep(1000)
		bot(18).servo_speed(-75)
		bot(19).servo_speed(-75)
		display.show(Image.ARROW_E)
		sleep(600)
	elif left == 0 and right ==1:  #Obstacle on left
		bot(18).servo_speed(-75)	#backup for 1s, turn right
		bot(19).servo_speed(75)
		display.show(Image.ARROW_N)
		bot(15).write_digital(1)
		bot(0).write_digital(0)
		sleep(1000)
		bot(18).servo_speed(75)
		bot(19).servo_speed(75)
		display.show(Image.ARROW_W)
		sleep(600)
	elif left == 0 and right == 0: #Obstacle on left + right
		bot(18).servo_speed(-75)	#backup for 1s, turn
		bot(19).servo_speed(75)
		display.show(Image.ARROW_N)
		bot(15).write_digital(1)
		bot(0).write_digital(1)
		sleep(1000)
		bot(18).servo_speed(75)
		bot(19).servo_speed(75)
		display.show(Image.ARROW_W)
		sleep(1000)