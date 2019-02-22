# group_io.py  v_0_5_0
from cyberbot import *
class io():
	def __init__(self,p=0,q=33):
		self.pA=p
		self.pB=q
	def states(self,s):
		if s is None:
			bot(self.pA,self.pB).send_c(8)
			return bot().read_r()
		else:bot(self.pA,self.pB).send_c(7,s)
	def directions(self,d):
		if d is None:
			bot(self.pA,self.pB).send_c(6)
			return bot().read_r()
		else:bot(self.pA,self.pB).send_c(5,d)
