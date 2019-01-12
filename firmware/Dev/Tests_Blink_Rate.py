# Test_Blink_Rate.py
# Use oscilloscope on P7 to measure cycle time

from microbit import *
from parallax import bot

while True:
    bot(7).digital_write(1)
    bot(7).digital_write(0)