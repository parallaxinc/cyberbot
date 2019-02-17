# Terminal_Display_AD.py

# Setup
#
#   o  Open cyberbot.py from: 
#	     Parallax Library (Editors without Files)
#   o  Copy all of it and paste over from cyberbot import * 

from cyberbot import *

bot(22).pitch(300, 2000)

while True:
    ad0 = pin0.read_analog()
    ad1 = pin1.read_analog()
    ad2 = pin2.read_analog()
    print('ad0 = %d, ad1 = %d, ad2 = %d' % (ad0, ad1, ad2))
    sleep(1000)