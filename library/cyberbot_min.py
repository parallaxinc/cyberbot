from microbit import *
class bot():
	def __init__(self,p,a=0x5D):
		self.addr=a
		self.pin=p
		while True:
			try:i2c.read(a,1)
			except OSError:pass
			else:
				i2c.write(a,bytes([0,99]));sleep(10)	 
				pin8.write_digital(1);sleep(10)	 
				while True:
					try:i2c.read(a,1)
					except OSError:pass
					else:break
				break
	def send_c(self,c,p=0,s=0,d=None,f=None):
		a=bytes([1,self.pin,p,s])
		if d is not None:a=a+d.to_bytes(4,'little')
		if f is not None:a=a+f.to_bytes(4,'little')
		i2c.write(self.addr,a)
		i2c.write(self.addr,bytes([0,c]))
		c=b'\x01'
		while c!=b'\x00':
			i2c.write(self.addr,b'\x00')
			c=i2c.read(self.addr,1)
	def read_r(self):
		i2c.write(self.addr,b'\x18')
		r=i2c.read(self.addr,4)
		return int.from_bytes(r,'little')
	def digital_write(self,s):
		if s>1 or s<0:s=4
		elif s==0:s=2
		self.send_c(s)
	def analog_write(self,f,c=0):self.send_c(32,c,0,f)
	def digital_read(self):
		self.send_c(3)
		return self.read_r()
	def states(self,p,s):
		if p>self.pin:raise ValueError('start > end!')
		elif self.pin-p>8:raise ValueError('> 8 pins!')
		elif p==self.pin and s is None:return self.digitalRead()
		elif p==self.pin:self.digital_write(s&1)
		elif s is None:
			self.send_c(8,p)
			return self.read_r()
		else:self.send_c(7,p,s)
	def directions(self,p,d):
		if p>self.pin:raise ValueError('start > end!')
		elif self.pin-p>8:raise ValueError('> 8 pins!')
		elif d is None:
			self.send_c(6,p)
			return self.r()
		else:self.send_c(5,p,d)
	def qti(self,p,d=None):
		if p>self.pin:raise ValueError('start > end!')
		else:
			self.send_c(33,p,0,d)
			return self.read_r()
	def pulse_out(self,d):self.send_c(11,0,0,d)
	def pulse_in(self,s):
		self.send_c(10,0,s)
		return self.read_r()
	def pulse_count(self,d):
		self.send_c(12,0,0,d)
		return self.read_r()
	def rc_time(self,s,d=None,f=None,c=0):
		self.send_c(16,c,s,d,f)
		return self.read_r()
	def frequency_out(self,d,f):
		self.send_c(13,0,0,d,f)
	def ir_detect(self,p,f):
		self.send_c(31,p,0,f)
		return self.read_r()
	def servo_angle(self,v):self.send_c(24,0,0,v)
	def servo_speed(self,v):self.send_c(25,0,0,v)
	# def servo_set(self,v):self.send_c(26,0,0,v)
	def servo_ramping(self,v):self.send_c(27,0,0,v)
	def servo_disable(self):self.send_c(28)
	def ping_distance(self,u=None):
		self.send_c(29)
		d=self.read_r()
		if u is None:return d
		elif u=='in':return d/148
		else:return d/58
	def tv_remote(self):
		self.send_c(30)
		return self.read_r()
