# microbit-module: tv_remote@0.8.0
from cyberbot import *
class ir():
	def __init__(self,p=0):
		self.pin=p
	def remote(self):
		bot(self.pin).send_c(30)
		n=bot().read_r()
		if n==0xFFFFFFFF:
			n=-1
		return n