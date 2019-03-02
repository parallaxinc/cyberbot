# IR_Roam_Avoid_Obstacles.py

from cyberbot import *

bot(22).tone(2000, 300)

while True:

	irL = bot(14, 13).ir_detect(37500)
	irR = bot(1, 2).ir_detect(37500)

	bot(20).write_digital(irL)
	bot(21).write_digital(irR)

	if irL == 1 and irR == 1:
		bot(18).servo_speed(64)
		bot(19).servo_speed(-64)
		display.show(Image.HAPPY)
	elif irL == 0 and irR == 0:
		bot(18).servo_speed(-64)
		bot(19).servo_speed(64)
		display.show(Image.SAD)
	elif irL == 0:
		bot(18).servo_speed(64)
		bot(19).servo_speed(64)
		display.show(Image.SAD)
	elif irR == 0:
		bot(18).servo_speed(-64)
		bot(19).servo_speed(-64)
		display.show(Image.SAD)