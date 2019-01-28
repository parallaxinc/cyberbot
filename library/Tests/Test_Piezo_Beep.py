# Test_Piezo_Beep.py

from parallax import *

bot(22).frequency_out(300, 2000)

bot().disconnect()
