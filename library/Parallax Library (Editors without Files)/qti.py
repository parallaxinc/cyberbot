# qti.py v_0_3_9
# Replace  from qti import *  with this:

class qti():
	def __init__(self,p=0):
		self.pin=p
	def read_to(self,p,d=None):
		if p>self.pin:raise ValueError('start > end!')
		else:
			bot(self.pin).send_c(33,p,0,d)
			return bot().read_r()
