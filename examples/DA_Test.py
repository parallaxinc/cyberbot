# DA_Test.py

# Procedure: Observe D/A0 and D/A1 output lights

from parallax import *

bot(22).frequency_out(300, 2000)

while True:
    for da in range(0, 1025, 64):
        print("da = %d" % da)
        bot(20).analog_write(da)
        bot(21).analog_write(1024 - da)
        sleep(150)
        print(" ")
        sleep(500)