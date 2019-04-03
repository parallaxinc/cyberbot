# IR_Remote_Test.py			  #

from cyberbot import *
from tv_remote import *

bot(22).tone(2000, 300)

while True:
	num = ir(2).remote()
	if num > -1:
		display.scroll( str(num), 75, wait=False )
	sleep(100)