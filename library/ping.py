# v_0_3_7
#from parallax import send_c,read_r
from parallax import *
#import gc
class ping():
	def __init__(self,p=0):
		self.pin=p
	def distance(self,u=None):
		send_c(self.pin,29)
		d=read_r()
		if u is None:return d
		elif u=='in':return d/148
		else:return d/58
