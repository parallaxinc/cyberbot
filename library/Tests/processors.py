# ping.py v_0_3_9
from cyberbot import *

class pc():
	def __init__(self,p=0):
		self.pin=p
	def abc(self):
		bot(self.pin).send_c(30)
		return bot().read_r()

bot(22).pitch(200, 2000)
while True:
    f = pc().abc()
    print("f=%d" % f)
    sleep(1000)