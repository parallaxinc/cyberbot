# tv_remote.py v_0_5_0
from cyberbot import *
class ir():
	def __init__(self,p=0):
		self.pin=p
	def remote(self):
		bot(self.pin).send_c(30)
		return bot().read_r()