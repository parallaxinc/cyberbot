# v_0_3_7
#from parallax import send_c,read_r
from parallax import *
#import gc
class qti():
	def __init__(self,p=0):
		self.pin=p
	def read_to(self,p,d=None):
		if p>self.pin:raise ValueError('start > end!')
		else:
			send_c(self.pin,33,p,0,d)
			return read_r()
