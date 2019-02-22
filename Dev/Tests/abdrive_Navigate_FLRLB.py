# Navigate_FLRLB.py

# Setup
#
#   If your editor has a Files feature, use it to copy all .py files from:
#	  Parallax Library (Editors with Files)
#   to your micro:bit module's file system.

from cyberbot import *
from ab360 import *

bot(22).pitch(300, 2000)

drive.connect()

drive.goto(128,128)
drive.goto(32,-32)
drive.goto(-64,64)
drive.goto(32,-32)
drive.goto(-128,-128)

bot().disconnect()