# Terminal_Display_Up_Count.py

# Setup
#
#   o  Open cyberbot.py from: 
#	     Parallax Library (Editors without Files)
#   o  Copy all of it and paste over from cyberbot import * 

from cyberbot import *

bot(22).pitch(300, 2000)

counter = 0

print('hello!!!\n')

while True:
    print('counter = %d'  % counter)
    counter = counter + 1
    sleep(500)