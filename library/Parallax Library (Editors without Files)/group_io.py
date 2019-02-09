# group_io.py v_0_3_8
# Replace  from group_io import *  with this:

class io():
	def __init__(self,p=0):
		self.pin=p
	def states(self,p,s):
		if p>self.pin:raise ValueError('start > end!')
		elif self.pin-p>8:raise ValueError('> 8 pins!')
		elif p==self.pin and s is None:return self.digitalRead()
		elif p==self.pin:self.write_digital(s&1)
		elif s is None:
			send_c(self.pin,8,p)
			return read_r()
		else:send_c(self.pin,7,p,s)
	def directions(self,p,d):
		if p>self.pin:raise ValueError('start > end!')
		elif self.pin-p>8:raise ValueError('> 8 pins!')
		elif d is None:
			send_c(self.pin,6,p)
			return read_r()
		else:send_c(self.pin,5,p,d)
