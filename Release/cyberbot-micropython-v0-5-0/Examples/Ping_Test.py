##################################
# Ping_Test.py                   #
##################################

# Setup
#
#   If your editor has a Files feature, use it to copy all .py files from:  
#	  Parallax Library (Editors with Files) 
#   to your micro:bit module's file system.

from cyberbot import *
from ping import *

bot(22).pitch(300, 2000)

while True:
    distance = ping(8).distance(u="cm")
    print('dist = %d' % distance)
    display.scroll(str(distance), 125)
    sleep(750)