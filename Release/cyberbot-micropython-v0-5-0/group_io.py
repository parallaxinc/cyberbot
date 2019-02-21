# group_io.py v_0_4_0
from cyberbot import *
class io():
	def __init__(self,p=0,q=33):
		self.pA=p
		self.pB=q
	def states(self,s):
		#if p>self.pin:raise ValueError('start > end!')
		#elif self.pin-p>8:raise ValueError('> 8 pins!')
		#if self.pA==self.pB and s is None:return self.digitalRead()
		#if self.pA==self.pB:self.write_digital(s&1)
		if s is None:
			bot(self.pA,self.pB).send_c(8)
			return bot().read_r()
		else:bot(self.pA,self.pB).send_c(7,s)
	def directions(self,d):
		#if p>self.pin:raise ValueError('start > end!')
		#elif self.pin-p>8:raise ValueError('> 8 pins!')
		if d is None:
			bot(self.pA,self.pB).send_c(6)
			return bot().read_r()
		else:bot(self.pA,self.pB).send_c(5,d)
