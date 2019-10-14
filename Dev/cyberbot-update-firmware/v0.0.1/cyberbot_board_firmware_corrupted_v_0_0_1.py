from microbit import *
import os

new_firmware_version = 00001
file_size_bytes = 2444
filename = "cbbfwdoa.bin"

def check_i2c():
	try:i2c.read(93,1)
	except OSError:print("i2c no read");return 0
	else:
		pin8.set_pull(pin8.PULL_UP);sleep(10)	
		i2c.write(93,b'\0c');sleep(10)	
		while True:
			try:i2c.read(93,1)
			except OSError:print("i2c no reply");return 1
			else:print("i2c ok");return 2

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
	def detach(self):
		while True:
			bot(25).read_digital()

def version_info(v=0):
	if v is 0:
		result = 0
		for n in range(0, 40):
			result = check_i2c()
			print("result = %d" % result)
			sleep(50)
			if result == 2:break
		if result != 2:
		    print("Set PWR to 1.")
		    display.show("Set PWR to 1")
		bot().send_c(98)
		v = bot().read_r()
	print("v=%d" % v)
	p=v%100
	mi=((v%10000)-p)/100
	ma=((v%1000000)-mi-p)/10000
	return ma, mi, p

def version_in_board():
	ma, mi, p = version_info()
	print("v:%d.%d.%d" %(ma, mi, p))
	display.show("v%d.%d.%d" %(ma, mi, p))
	reset()

def version_of_updater():
	ma, mi, p = version_info(new_firmware_version)
	print("v:%d.%d.%d" %(ma, mi, p))
	display.show("v%d.%d.%d" %(ma, mi, p))
	reset()

def update_firmware():
	ee_i2c_addr = 80
	ee_mem_addr = 0
	mem_addr = 0

	pin8.write_digital(1)
	sleep(1)

	f = open(filename, "rb")

	buf = bytearray(128)

	reps = file_size_bytes // 128
	#print("Please wait, counting to %d..." % reps)
	reps = reps + 1

	#inc = reps // 25
	#print("reps=%d, inc=%d" %(reps, inc))
	n = 0

	for m in range(0, reps):
		n = reps - m - 1
		print("%d" % n)
#		if (m % inc) == 0:
#			if(n < 25):
#				display.set_pixel(4-(n%5),4-(n//5),5)
#				n=n+1
		f.readinto(buf, 128)
		ee_mem_addr = mem_addr.to_bytes(2, 'big')
		packet = ee_mem_addr + buf
		i2c.write(ee_i2c_addr, packet, False)
		mem_addr += 128
		sleep(100)

	partial = file_size_bytes % 128
	f.readinto(buf, partial)
	reps = reps - 1
	mem_addr = reps * 128
	ee_mem_addr = mem_addr.to_bytes(2, 'big')
	packet = ee_mem_addr + buf
	i2c.write(ee_i2c_addr, packet, False)

	f.close()

	sleep(100)

	display.show(" Done.", 600)
	display.show("Set PWR to 0. Unplug USB. ", 600, loop=True)

	reset()
