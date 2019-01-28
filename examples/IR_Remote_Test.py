##################################
# IR_Remote_Test.py              #
# IR detector connected to pin 2 #
##################################

from parallax import *
from tv_remote import *

bot(22).frequency_out(300, 2000)

while True:
    num = ir(2).remote()
    if num < 1000:
        display.scroll( str(num), 75, wait=False )
    sleep(100)