# Test_Piezo_Beep_Then_Loop.py

from cyberbot import *

bot(22).tone(2000, 300)

while True:
	bot(0).write_digital(1)
	bot(0).write_digital(0)