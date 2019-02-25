# digital_write_read.py

from cyberbot import *

bot(22).tone(2000, 300)

while True:

	while True:
		bot(0).write_digital(1)
		bot(15).write_digital(0)
		sleep(500)
		bot(0).write_digital(0)
		bot(15).write_digital(1)
		sleep(500)
		bot(0).write_digital(0)
		bot(15).write_digital(0)
		sleep(500)
		bot(0).write_digital(1)
		bot(15).write_digital(1)
		p7 = bot(7).read_digital()
		p9 = bot(9).read_digital()
		sleep(500)
		p0 = bot(0).read_digital()
		# sleep(10)
		# p0 = bot(0).read_digital()
		sleep(500)
		p15 = bot(15).read_digital()
		# sleep(10)
		# p15 = bot(15).read_digital()
		sleep(500)
		print("p0:%d,p7:%d,p9:%d,p15:%d" % (p0,p7,p9,p15))
		bot(22).tone(100, 2000)