# microbit-module: cyberbot@0.9.2
from microbit import *
while True:
	try:i2c.read(93,1)
	except OSError:pass
	else:
		pin8.set_pull(pin8.PULL_UP);sleep(10)	
		i2c.write(93,b'\0c');sleep(10)	
		while True:
			try:i2c.read(93,1)
			except OSError:pass
			else:break
		break
sleep(500)
class bot():
	def __init__(self,p=27,q=33):
		self.pA=p
		self.pB=q
	def botdisable(self):
		pin8.set_pull(pin8.NO_PULL)
		sleep(200)
		reset()
	def send_c(self,c,s=0,d=None,f=None):
		a=bytes([1,self.pA,self.pB,s])
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
			self.botdisable()
	def read_r(self):
		try:
			i2c.write(93,b'\x18')
			r=i2c.read(93,4)
			return int.from_bytes(r,'little')
		except:
			self.botdisable()
	def write_digital(self,s):
		if s>1 or s<0:s=4
		elif s==0:s=2
		self.send_c(s)
	def write_analog(self,f):self.send_c(32,0,f)
	def read_digital(self):
		self.send_c(3)
		return self.read_r()
	def pulse_out(self,d):self.send_c(11,0,d)
	def pulse_in(self,s):
		self.send_c(10,s)
		return self.read_r()
	def pulse_count(self,d):
		self.send_c(12,0,d)
		return self.read_r()
	def rc_time(self,s,d=None,f=None):
		self.send_c(16,s,d,f)
		return self.read_r()
	def tone(self,f,d):
		self.send_c(13,0,d,f)
	def ir_detect(self,f):
		bot(self.pB,self.pA).send_c(31,0,f)
		return self.read_r()
	def servo_angle(self,v=None):
		if v is None:c=28 
		else:c=24
		self.send_c(c,0,v)
	def servo_speed(self,vL=None,vR=None):
		if vL is None:c=28
		else:c=25
		self.send_c(c,0,vL,vR)
	def servo_accelerate(self,a):self.send_c(27,0,a)
	def detach(self):
		while True:
			bot(25).read_digital()