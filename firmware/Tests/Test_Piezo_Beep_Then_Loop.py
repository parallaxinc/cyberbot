# Test_Piezo_Beep_Then_Loop.py

from parallax import *

bot(22).frequency_out(300, 2000)

while True:
    bot(21).digital_write(1)
    bot(21).digital_write(0)