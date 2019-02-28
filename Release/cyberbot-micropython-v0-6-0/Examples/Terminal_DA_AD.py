# Terminal_DA_AD.py

# Circuit
#   D/A0---A/D0, D/A1---A/D1,
#   pot A---3.3V, potB---GND, pot wiper---A/D2

# Procedure
#   Run, then open REPL and then CTRL + D
#   Twist pot input while program runs to see ad2 vary

# Notes
#   micro:bit ground is 0.4 V below cyber:bot board ground
#   micro:bit 3.3 V = 3.245 V WRT cyber:bot board ground
#   cyber:bot 3.3 V = 3.326 V WRT cyber:bot board ground

# Output example
#   da0 = 0, da1 = 1024, ad0 = 13, ad1 = 623, ad2 = 7
#   da0 = 64, da1 = 960, ad0 = 72, ad1 = 998, ad2 = 7
#   da0 = 128, da1 = 896, ad0 = 137, ad1 = 934, ad2 = 7
#   da0 = 192, da1 = 832, ad0 = 203, ad1 = 871, ad2 = 7
#   da0 = 256, da1 = 768, ad0 = 266, ad1 = 805, ad2 = 87
#   da0 = 320, da1 = 704, ad0 = 332, ad1 = 744, ad2 = 150
#   da0 = 384, da1 = 640, ad0 = 398, ad1 = 680, ad2 = 211
#   da0 = 448, da1 = 576, ad0 = 461, ad1 = 617, ad2 = 261
#   da0 = 512, da1 = 512, ad0 = 526, ad1 = 554, ad2 = 308
#   da0 = 576, da1 = 448, ad0 = 588, ad1 = 490, ad2 = 372
#   da0 = 640, da1 = 384, ad0 = 652, ad1 = 425, ad2 = 469
#   da0 = 704, da1 = 320, ad0 = 716, ad1 = 360, ad2 = 629
#   da0 = 768, da1 = 256, ad0 = 779, ad1 = 295, ad2 = 806
#   da0 = 832, da1 = 192, ad0 = 845, ad1 = 231, ad2 = 867
#   da0 = 896, da1 = 128, ad0 = 907, ad1 = 165, ad2 = 947
#   da0 = 960, da1 = 64, ad0 = 970, ad1 = 100, ad2 = 1023

from cyberbot import *

bot(22).tone(2000, 300)

while True:
	for da in range(0, 1024, 64):

		bot(20).write_analog(da)
		bot(21).write_analog(1024 - da)
		sleep(20)

		ad0 = pin0.read_analog()
		ad1 = pin1.read_analog()
		ad2 = pin2.read_analog()

		print("da0 = %d, da1 = %d, ad0 = %d, ad1 = %d, ad2 = %d" % (da, 1024 - da, ad0, ad1, ad2))
		sleep(150)

	print(" ")
	sleep(500)