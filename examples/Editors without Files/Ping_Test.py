##################################
# Ping_Test.py                   #
##################################

# Setup
#
#   o  Open cyberbot.py from: 
#	     Parallax Library (Editors without Files)
#   o  Copy all of it and paste over from cyberbot import * 
#	o  Open ping.py from the same folder and paste it over from ping import *

from cyberbot import *
from ping import *

bot(22).pitch(300, 2000)

while True:
    distance = ping(8).distance(u="cm")
    print('dist = %d' % distance)
    display.scroll(str(distance), 125)
    sleep(750)