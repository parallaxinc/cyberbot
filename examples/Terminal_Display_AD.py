# Terminal_Display_AD.py

from parallax import *

bot(22).frequency_out(300, 2000)

while True:
    ad0 = pin0.read_analog()
    ad1 = pin1.read_analog()
    ad2 = pin2.read_analog()
    print('ad0 = %d, ad1 = %d, ad2 = %d' % (ad0, ad1, ad2))
    sleep(1000)