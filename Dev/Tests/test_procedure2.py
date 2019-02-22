# test_procedure_10002.py
# Connect P15..P8 to P7..P0, D/A0,1 to A/D0,1 A/D2 to 2.5 V
# Load micro:bit

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
class bot():
	def __init__(self,p=0):
		self.pin=p
	def botdisable(self):
		pin8.set_pull(pin8.NO_PULL)
		sleep(200)
		reset()
	def send_c(self,c,p=33,s=0,d=None,f=None):
		a=bytes([1,self.pin,p,s])
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
	def write_analog(self,f):self.send_c(32,0,0,f)
	def read_digital(self):
		self.send_c(3)
		return self.read_r()
	def pitch(self,d,f):
		self.send_c(13,0,0,d,f)
	def version_info(self):
		self.send_c(98)
		return self.read_r()

class io():
	def __init__(self,p=0):
		self.pin=p
	def states(self,p,s):
		if p>self.pin:raise ValueError('start > end!')
		elif self.pin-p>8:raise ValueError('> 8 pins!')
		elif p==self.pin and s is None:return self.digitalRead()
		elif p==self.pin:self.write_digital(s&1)
		elif s is None:
			bot(self.pin).send_c(8,p)
			return bot().read_r()
		else:bot(self.pin).send_c(7,p,s)
	def directions(self,p,d):
		if p>self.pin:raise ValueError('start > end!')
		elif self.pin-p>8:raise ValueError('> 8 pins!')
		elif d is None:
			bot(self.pin).send_c(6,p)
			return bot().read_r()
		else:bot(self.pin).send_c(5,p,d)

def fail(code):
	bot(25).write_digital(1)
	display.show(code)
	x = 0
	while True:
		x = x + 1


n = bot().version_info()

if n != 10002:fail(1)

display.off()
ad4 = pin4.read_analog()
display.on()
v = ad4 * (3.3 - 0.090) / 1024
v = v * (64.9 / 10.0)
# print("v = %f" % v)
if v < 6.0 or v > 15.0:fail(2)

bot(20).write_analog(102);
sleep(10)
ad = pin0.read_analog()
if ad < 30 or ad > 162:fail(3)

bot(20).write_analog(900);
sleep(10)
ad = pin0.read_analog()
if ad < 830 or ad > 960:fail(4)

bot(21).write_analog(102);
sleep(10)
ad = pin1.read_analog()
if ad < 30 or ad > 162:fail(5)

bot(21).write_analog(900);
sleep(10)
ad = pin1.read_analog()
if ad < 830 or ad > 960:fail(6)

ad = pin2.read_analog()
if ad < 700 or ad > 850:fail(7)

io(7).directions(0, 0)
io(15).states(8, 170)
io(15).directions(8, 255)
x = io(7).states(0, None)
if x != 170:fail(8)

io(15).directions(8, 0)
io(7).states(0, 85)
io(7).directions(0, 255)
x = io(15).states(8, None)
if x != 85:fail(9)

io(19).directions(18, 0)
io(17).states(16, 2)
io(17).directions(16, 3)
x = io(19).states(18, None)
if x != 2:fail(10)

io(17).directions(16, 0)
io(19).states(18, 1)
io(19).directions(18, 3)
x = io(17).states(16, None)
if x != 1:fail(11)

f = 500

while True:
	bot(20).write_digital(1)
	bot(22).pitch(100, f)
	sleep(200)
	bot(20).write_digital(0)
	bot(21).write_digital(1)
	sleep(300)
	bot(21).write_digital(0)
	f = f + 500
	if f > 3000: f = 500