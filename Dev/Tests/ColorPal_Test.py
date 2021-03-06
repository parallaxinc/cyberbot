# ColorPal_Test.py

# IMPORTANT: Connect directly to the micro:bit's pin2 and pin1.

#         diode
#         0.7 V
# pin2 -- anode
# pin1 -- cahtode -- colorpal signal

from cyberbot import *

bot(22).tone(2000, 200)

while True:
	pin1.write_digital(0)
	sleep(10)
	pin1.read_digital()
	while pin2.read_digital() == 0:pass
	pin1.write_digital(0)
	sleep(80)
	pin1.read_digital()
	sleep(10)
	uart.init(baudrate=4800, tx=pin1, rx=pin2)
	c=b'=(00 $ m)!'
	uart.write(c)
	sleep(10)
	if uart.any():
		val = uart.read()
		sleep(120)
		val = uart.read()
		uart.init(115200)
		if val is not None:
			i = val.find(b'$')
			r = int(val[i+1:i+4],16)
			g = int(val[i+4:i+7], 16)
			b = int(val[i+7:i+10],16)
			print("r = %d, g = %d, b = %d" % (r, g, b))