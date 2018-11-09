# Test_Blink_Rate.py
# Use oscilloscope on P7 to measure cycle time

while True:
    bot(7).digital_write(1)
    bot(7).digital_write(0)