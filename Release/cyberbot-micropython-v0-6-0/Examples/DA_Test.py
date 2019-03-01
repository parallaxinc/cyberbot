# DA_Test.py

from cyberbot import *

bot(22).tone(2000, 300)

while True:
	for da in range(0, 1025, 64):
		print("da = %d" % da)
		bot(20).write_analog(da)
		bot(21).write_analog(1024 - da)
		sleep(250)