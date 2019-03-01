# IR_Remote_Control_Expanded.py

from cyberbot import *
from tv_remote import *

bot(22).tone(2000, 300)

while True:
	num = ir(2).remote()
	# Forward on button press 1
	if num == 1:
		bot(18).servo_speed(0)
		bot(19).servo_speed(-75)
		display.show(Image.ARROW_SE)
	elif num == 2:
		bot(18).servo_speed(75)
		bot(19).servo_speed(-75)
		display.show(Image.ARROW_S)
	elif num == 3:
		bot(18).servo_speed(75)
		bot(19).servo_speed(0)
		display.show(Image.ARROW_SW)
	elif num == 4:
		bot(18).servo_speed(-75)
		bot(19).servo_speed(-75)
		display.show(Image.ARROW_E)
	elif num == 5:
		bot(18).servo_speed(0)
		bot(19).servo_speed(0)
		display.show(Image.HAPPY)
	elif num == 6:
		bot(18).servo_speed(75)
		bot(19).servo_speed(75)
		display.show(Image.ARROW_W)
	elif num == 7:
		bot(18).servo_speed(0)
		bot(19).servo_speed(75)
		display.show(Image.ARROW_NE)
	elif num == 8:
		bot(18).servo_speed(-75)
		bot(19).servo_speed(75)
		display.show(Image.ARROW_N)
	elif num == 9:
		bot(18).servo_speed(-75)
		bot(19).servo_speed(0)
		display.show(Image.ARROW_NW)