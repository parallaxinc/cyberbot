# IR_Follow_Leader_with_DA_and_IR_Tuning.py

# Tune it!
# Servos need to be well centered, and IR LEDs and
# receivers need to be pointed straight forward.  Also, don't
# for get to use D/A0 for the P14 IR LED's cathod, and D/A1 for
# the P1 IRLED's cathode.  Next, run in position 1 and use a
# flat object swept closer to cyber:bot's front, and determine
# which side's bar graph lights go out first.  That'll be the
# side with the dimL/R variable to increase.  Keep adjusting
# till the LED lights disappear at almost the same rate as
# you move the flat object toward the front of the cyber:bot.

from cyberbot import *

# Correct IR sensor mismatch by increasing the dim on the side where
# the lights go out sooner as the obstacle gets closer. (0...500)
dimL	 = 0
dimR	 = 0

# Increase negative value for more peppy, decrease for less spastic.
kp	   = -30

# Increase slower forward faster backward.  Decrease is opposite.
setPoint = 3

# Adjustments not needed.
errorL   = 0
errorR   = 0
driveL   = 0
driveR   = 0

bot(22).tone(2000, 300)

while True:

	# Check obstacle distances
	irL = 0
	irR = 0
	for da in range(510, 0, -102):
		bot(20).write_analog(da + dimL)
		bot(21).write_analog(da + dimR)
		irL += bot(14, 13).ir_detect(38000)
		irR += bot(1, 2).ir_detect(38000)

	# Display obstacle distance
	display.clear()
	for n in range(0, irL, 1):
		display.set_pixel(4, n, 5)
	for n in range(0, irR, 1):
		display.set_pixel(0, n, 5)

	# Control system calculations - proportional
	errorL = setPoint - irL
	errorR = setPoint - irR
	driveL = kp * errorL
	driveR = -kp * errorR

	# Set CR servo speeds
	bot(18).servo_speed(driveL)
	bot(19).servo_speed(driveR)