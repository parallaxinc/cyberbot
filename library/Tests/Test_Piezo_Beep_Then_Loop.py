# Test_Piezo_Beep_Then_Loop.py

from cyberbot import *

bot(22).pitch(300, 2000)

while True:
    bot(21).write_digital(1)
    bot(21).write_digital(0)