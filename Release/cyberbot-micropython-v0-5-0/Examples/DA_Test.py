# DA_Test.py

# Setup
#
#   If your editor has a Files feature, use it to copy all .py files from:
#	  Parallax Library (Editors with Files)
#   to your micro:bit module's file system.

# Procedure: Observe D/A0 and D/A1 output lights

from cyberbot import *

bot(22).pitch(300, 2000)

while True:
    for da in range(0, 1025, 64):
        print("da = %d" % da)
        bot(20).write_analog(da)
        bot(21).write_analog(1024 - da)
        sleep(250)