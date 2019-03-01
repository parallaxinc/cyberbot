# Terminal_AD_and_Bat.py

from cyberbot import *

bot(22).tone(2000, 300)

display.off()

while True:
	ad0 = pin0.read_analog()
	ad1 = pin1.read_analog()
	ad2 = pin2.read_analog()
	ad4 = pin4.read_analog()

	print('ad0 = %d, ad1 = %d, ad2 = %d, ad4 = %d' % (ad0, ad1, ad2, ad4))
	sleep(1000)