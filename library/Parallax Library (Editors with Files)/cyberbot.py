# cyberbot.py v_0_3_8
from microbit import *
while True:
	try:i2c.read(93,1)
	except OSError:pass
	else:
		pin8.set_pull(pin8.PULL_UP)	
		i2c.write(93,b'\0c');sleep(10)	
		while True:
			try:i2c.read(93,1)
			except OSError:pass
			else:break
		break
def botdisable():
	pin8.set_pull(pin8.NO_PULL)
	sleep(100)
	reset()
def send_c(pin,c,p=33,s=0,d=None,f=None):
	a=bytes([1,pin,p,s])
	if d is not None:a+=(round(d)).to_bytes(4,'little')
	if f is not None:a+=(round(f)).to_bytes(4,'little')
	try:
		i2c.write(93,a)
		i2c.write(93,bytes([0,c]))
		c=b'\x01'
		while c!=b'\0':
			i2c.write(93,b'\0')
			c=i2c.read(93,1)
	except:
		botdisable()
def read_r():
	try:
		i2c.write(93,b'\x18')
		r=i2c.read(93,4)
		return int.from_bytes(r,'little')
	except:
		botdisable()
class bot():
	def __init__(self,p=0):
		self.pin=p
	def write_digital(self,s):
		if s>1 or s<0:s=4
		elif s==0:s=2
		send_c(self.pin,s)
	def write_analog(self,f):send_c(self.pin,32,0,0,f)
	def read_digital(self):
		send_c(self.pin,3)
		return read_r()
	def pulse_out(self,d):send_c(self.pin,11,0,0,d)
	def pulse_in(self,s):
		send_c(self.pin,10,0,s)
		return read_r()
	def pulse_count(self,d):
		send_c(self.pin,12,0,0,d)
		return read_r()
	def rc_time(self,s,d=None,f=None,c=0):
		send_c(self.pin,16,c,s,d,f)
		return read_r()
	def pitch(self,d,f):
		send_c(self.pin,13,0,0,d,f)
	def ir_detect(self,p,f):
		send_c(self.pin,31,p,0,f)
		return read_r()
	def servo_angle(self,v):send_c(self.pin,24,0,0,v)
	def servo_speed(self,v,d=None):
		if d is None:send_c(self.pin,25,33,0,v,d)
		else:send_c(self.pin,25,self.pin+1,0,v,d)
	def servo_disable(self):send_c(self.pin,28)
	def disconnect(self):
		while True:
			bot(25).read_digital()