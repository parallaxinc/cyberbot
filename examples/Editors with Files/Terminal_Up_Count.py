# Terminal_Display_Up_Count.py

# Setup
#
#   If your editor has a Files feature, use it to copy all .py files from:  
#	  Parallax Library (Editors with Files) 
#   to your micro:bit module's file system.

from cyberbot import *

bot(22).pitch(300, 2000)

counter = 0

print('hello!!!\n')

while True:
    print('counter = %d'  % counter)
    counter = counter + 1
    sleep(500)