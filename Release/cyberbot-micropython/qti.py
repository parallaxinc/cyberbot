# microbit-module: qti@0.8.0
from cyberbot import *
class qti():
	def __init__(self,p=0,q=33):
		self.pA=p
		self.pB=q
	def read(self,d=None):
		#if self.pB>self.pA:raise ValueError('start > end!')
		#else:
		bot(self.pA,self.pB).send_c(33,0,d)
		return bot().read_r()
