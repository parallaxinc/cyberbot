##################################
# Ping_Test.py                   #
##################################

from parallax import *

while True:
    dist = bot(8).ping_distance(u="cm")
    display.scroll(str(dist), 125)
    # print('dist = %d' % dist)    