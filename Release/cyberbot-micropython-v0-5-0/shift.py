# shift.py v_0_3_9
from cyberbot import *
class shift():
	def __init__(self,p=33,q=33):
		self.pA=p
		self.pB=q
	def send(self,s,b,d):
		bot(self.pA,self.pB).send_c(18,s,b,d)
	def receive(self,s,b):
		bot(self.pA,self.pB).send_c(17,s,b)
		return bot().read_r()