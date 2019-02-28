# Navigate_Routine_Long.py
from cyberbot import *

bot(22).tone(2000, 300)

# 96 if you leave it connected.
# directions = 'FBLRSLRFLRSFBLRSLRFLRSFBLRSLRFLRSFBLRSLRFLRSFBLRSLRFLRSFBLRSLRFLRSFBLRSLRFLRSFBLRSLRFLRSFBLRSLRF'
# durations =  [3,2,.5,.5,1.5,.5,1,.5,.5,.5,3,3,2,.5,.5,1.5,.5,1,.5,.5,.5,3,3,2,.5,.5,1.5,.5,1,.5,.5,.5,3,3,2,.5,.5,1.5,.5,1,.5,.5,.5,3,3,2,.5,.5,1.5,.5,1,.5,.5,.5,3,3,2,.5,.5,1.5,.5,1,.5,.5,.5,3,3,2,.5,.5,1.5,.5,1,.5,.5,.5,3,3,2,.5,.5,1.5,.5,1,.5,.5,.5,3,3,2,.5,.5,1.5,.5,1,.5,.5,.5]

# 145 if you disconnect and restart.
# directions = 'FBLRSLRFLRSFBLRSLRFLRSFBLRSLRFLRSFBLRSLRFLRSFBLRSLRFLRSFBLRSLRFLRSFBLRSLRFLRSFBLRSLRFLRSFBLRSLRFBLRSLRFLRSFBLRSLRFBLRSLRFLRSFBLRSLRFBLRSLRFLRSFBL'
# durations =  [3,2,.5,.5,1.5,.5,1,.5,.5,.5,3,3,2,.5,.5,1.5,.5,1,.5,.5,.5,3,3,2,.5,.5,1.5,.5,1,.5,.5,.5,3,3,2,.5,.5,1.5,.5,1,.5,.5,.5,3,3,2,.5,.5,1.5,.5,1,.5,.5,.5,3,3,2,.5,.5,1.5,.5,1,.5,.5,.5,3,3,2,.5,.5,1.5,.5,1,.5,.5,.5,3,3,2,.5,.5,1.5,.5,1,.5,.5,.5,3,3,2,.5,.5,1.5,.5,1,.5,.5,.5,.5,1.5,.5,1,.5,.5,.5,3,3,2,.5,.5,1.5,.5,1,.5,.5,.5,.5,1.5,.5,1,.5,.5,.5,3,3,2,.5,.5,1.5]
# # 135 with 0.4.0 in Mu
directions = 'FBLRSLRFLRSFBLRSLRFLRSFBLRSLRFLRSFBLRSLRFLRSFBLRSLRFLRSFBLRSLRFLRSFBLRSLRFLRSFBLRSLRFLRSFBLRSLRFBLRSLRFLRSFBLRSLRFBLRSLRFLRSFBLRSLRFLRF'
durations =  [3,2,.5,.5,1.5,.5,1,.5,.5,.5,3,3,2,.5,.5,1.5,.5,1,.5,.5,.5,3,3,2,.5,.5,1.5,.5,1,.5,.5,.5,3,3,2,.5,.5,1.5,.5,1,.5,.5,.5,3,3,2,.5,.5,1.5,.5,1,.5,.5,.5,3,3,2,.5,.5,1.5,.5,1,.5,.5,.5,3,3,2,.5,.5,1.5,.5,1,.5,.5,.5,3,3,2,.5,.5,1.5,.5,1,.5,.5,.5,3,3,2,.5,.5,1.5,.5,1,.5,.5,.5,.5,1.5,.5,1,.5,.5,.5,3,3,2,.5,.5,1.5,.5,1,.5,.5,.5,.5,.5,.5]
# 96
#directions = 'FBLRSLRFLRSFBLRSLRFLRSFBLRSLRFLRSFBLRSLRFLRSFBLRSLRFLRSFBLRSLRFLRSFBLRSLRFLRSFBLRSLRFLRSFBLRSLR'
#durations =  [3,2,.5,.5,1.5,.5,1,.5,.5,.5,3,3,2,.5,.5,1.5,.5,1,.5,.5,.5,3,3,2,.5,.5,1.5,.5,1,.5,.5,.5,3,3,2,.5,.5,1.5,.5,1,.5,.5,.5,.5,3,3,2,2,.5,.5,1.5,.5,1,.5,.5,.5,3,3,2,.5,.5,1.5,.5,1,.5,.5,.5,3,3,2,.5,.5,1.5,.5,1,.5,.5,.5,.5]

for direction, duration in zip(directions, durations):
	if direction == 'F':
		display.show(Image.ARROW_S)
		bot(18, 19).servo_speed(50, -50)
	elif direction == 'B':
		display.show(Image.ARROW_N)
		bot(18, 19).servo_speed(-50, 50)
	elif direction == 'R':
		display.show(Image.ARROW_W)
		bot(18, 19).servo_speed(50, 50)
	elif direction == 'L':
		display.show(Image.ARROW_E)
		bot(18, 19).servo_speed(-50, -50)
	else:
		display.show(Image.SQUARE_SMALL)
		bot(18).servo_speed()
		bot(19).servo_speed()

	sleep(duration * 1000)

display.clear
bot(18).servo_speed()
bot(19).servo_speed()

bot(22).tone(500, 2000)

bot().detach()