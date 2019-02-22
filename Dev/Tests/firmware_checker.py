# firmware_checker.py v_0_4_0
from cyberbot import *
class firmware():
	def __init__(self):
		bot().send_c(98)
		self.v=bot().read_r()
	def version_info(self):
		#v=self.v
		p=self.v%100
		mi=((self.v%10000)-p)/100
		ma=((self.v%1000000)-mi-p)/10000
		print("Firmware: v%d.%d.%d" %(ma, mi, p))
		display.show("FW:v%d.%d.%d" %(ma, mi, p))
