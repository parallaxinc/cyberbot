# Firmware Load Test 0 3 4.py

from cyberbot import *

while True:

	bot(22).tone(2000, 300)

	display.off()
	ad4 = pin4.read_analog()
	display.on()

	print('ad4 = %d' % ad4)

	# The miro:bit supply has a low voltage diode for protection,
	# so it's A/D supply is 3.3 V - diode drop.
	v = ad4 * (3.3 - 0.090) / 1024	# Convert to volts
	v = v * (64.9 / 10.0)
	# Undo down-scaling that circuit on board performs for safe
	# measurements over 3.3 V

	bot(20).write_digital(1)
	sleep(500)
	bot(20).write_digital(0)
	sleep(100)

	bot(21).write_digital(1)
	sleep(500)
	bot(21).write_digital(0)
	sleep(100)

	bot(25).write_digital(1)
	sleep(500)
	bot(25).write_digital(0)
	sleep(100)

	if (v < 5.0) or (v > 9.0):
		bot(25).write_digital(1)

	print("Battery voltage: %f" % v)
	# display.show("Bat V: %2f" % v)

	bot(22).read_digital()
	sleep(200)
