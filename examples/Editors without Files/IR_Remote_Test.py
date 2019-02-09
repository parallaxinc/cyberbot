##################################
# IR_Remote_Test.py              #
# IR detector connected to pin 2 #
##################################

# Setup
#
#   o  Open cyberbot.py from: 
#	     Parallax Library (Editors without Files)
#   o  Copy all of it and paste over from cyberbot import * 
#	o  Open tv_remote.py from the same folder and paste it over from tv_remote import *

from cyberbot import *
from tv_remote import *

bot(22).pitch(300, 2000)

while True:
    num = ir(2).remote()
    if num < 1000:
        display.scroll( str(num), 75, wait=False )
    sleep(100)