##################################
# IR_Remote_Test.py              #
# IR detector connected to pin 2 #
##################################

from parallax import *

while True:
    num = bot(2).tv_remote()
    if num < 1000:
        display.scroll( str(num), 75, wait=False )
    sleep(100)