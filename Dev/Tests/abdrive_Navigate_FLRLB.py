# Navigate_FLRLB.py

from cyberbot import *
from ab360 import *

bot(22).tone(2000, 300)

drive.connect()

drive.goto(128,128)
drive.goto(32,-32)
drive.goto(-64,64)
drive.goto(32,-32)
drive.goto(-128,-128)

bot().detach()