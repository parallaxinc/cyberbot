# DA_Test.py

# Procedure
#   Twist pot input while program runs to see ad2 vary

from parallax import *

while True:
    for da in range(0, 1025, 64):
    print("da = %d" % da)
    bot(20).analog_write(da)
    bot(21).analog_write(1024 - da)
    sleep(150)
    print(" ")
    sleep(500)