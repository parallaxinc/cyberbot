# v_0_3_7
#from parallax import send_c,read_r
from parallax import *
#import gc
class ir():
	def __init__(self,p=0):
		self.pin=p
	def remote(self):
		send_c(self.pin,30)
		return read_r()