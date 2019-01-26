##################################
# Ping_Test.py                   #
##################################

from parallax import *

bot(22).frequency_out(300, 2000)

while True:
    dist = bot(8).ping_distance(u="cm")
    print('dist = %d' % dist)
    display.scroll(str(dist), 125)
    display.scroll(str(dist), 125)
    sleep(750)