# ping.py v_0_3_9
from cyberbot import *
class ping():
	def __init__(self,p=0):
		self.pin=p
	def distance(self,u=None):
		bot(self.pin).send_c(29)
		d=bot().read_r()
		if u is None:return d
		elif u=='in':return d/148
		else:return d/58