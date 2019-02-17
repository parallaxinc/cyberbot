# Navigate_FLRLB.py

# Setup
#
#   If your editor has a Files feature, use it to copy all .py files from:
#	  Parallax Library (Editors with Files)
#   to your micro:bit module's file system.

from cyberbot import *
print("1")

bot(22).pitch(300, 2000)
# bot(22).send_c(13,0,0,300,2000)
print("2")

# while True:
#    x = bot(17).pulse_in(1)
#    print("x = %d" % x)
#    sleep(1500)


bot(0).send_c(61)
print("3")

# drive360.connect()
# sleep(1000)
bot().send_c(62,0,0,100,100)
sleep(2000)
bot().send_c(62,0,0,0,0)
print("5")
# print("hello3")
# sleep(2000)
# bot().send_c(62,0,0,0,0)

bot().disconnect()