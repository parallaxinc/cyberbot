# microbit-module: i2c_repeat@0.7.0
from cyberbot import *
class i2c_repeat():
	def __init__(self,p=33,q=33):
		self.pA=p
		self.pB=q
	def connect(self):
		bot().send_c(40,0,self.pA,self.pB)
