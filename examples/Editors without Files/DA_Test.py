# DA_Test.py

# Procedure: Observe D/A0 and D/A1 output lights

# Setup
#
#   o  Open cyberbot.py from: 
#	     Parallax Library (Editors without Files)
#   o  Copy all of it and paste over from cyberbot import * 

from cyberbot import *

bot(22).pitch(300, 2000)

while True:
    for da in range(0, 1025, 64):
        print("da = %d" % da)
        bot(20).write_analog(da)
        bot(21).write_analog(1024 - da)
        sleep(150)
        print(" ")
        sleep(500)