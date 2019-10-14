# microbit-module: colorpal@0.8.0
from cyberbot import *
class colorpal():
	def __init__(self,p=33):
		self.pin=p
	def read(self,u=None):
		bot(self.pin).send_c(34)
		try:
			i2c.write(93,b'\x14')
			s=i2c.read(93,9)
			return int(s[0:3],16),int(s[3:6],16),int(s[6:9],16)
		except:
			bot.botdisable()
