##################################
# IR_Remote_Test.py              #
# IR detector connected to pin 2 #
##################################

# Setup
#
#   If your editor has a Files feature, use it to copy all .py files from:  
#	  Parallax Library (Editors with Files) 
#   to your micro:bit module's file system.

from cyberbot import *
from tv_remote import *

bot(22).pitch(300, 2000)

while True:
    num = ir(2).remote()
    if num < 1000:
        display.scroll( str(num), 75, wait=False )
    sleep(100)