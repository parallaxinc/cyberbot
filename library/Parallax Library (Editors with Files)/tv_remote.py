# tv_remote.py v_0_3_8
from cyberbot import *
class ir():
	def __init__(self,p=0):
		self.pin=p
	def remote(self):
		send_c(self.pin,30)
		return read_r()