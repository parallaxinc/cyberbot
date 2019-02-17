# Navigate_FBS.py

from cyberbot import *
from group_io import *

while True:

    bot(22).pitch(300, 1000)

    io(9).directions(6, 15)
    sleep(1000)

    for n in range(15, -1, -1):
        io(9).states(6, n)
        directions = io(9).directions(6, None)
        states = io(9).states(6, None)
        print("directions = %d" % directions)
        print("states = %d" % states)
        sleep(300)

    bot(22).pitch(300, 1500)

    io(9).states(6, 3)

    for n in range(15, -1, -1):
        io(9).directions(6, n)
        directions = io(9).directions(6, None)
        states = io(9).states(6, None)
        print("directions = %d" % directions)
        print("states = %d" % states)
        sleep(300)

    bot(22).pitch(300, 2000)

    io(9).states(6, 12)
    io(9).directions(6, 12)
    for n in range(1, 4, 1):
        io(9).directions(9,1)
        sleep(400)
        io(9).directions(9,0)
        sleep(400)
        io(9).states(8,1)
        sleep(400)
        io(9).states(8,0)
        sleep(400)

    io(9).states(8,0)
    bot(22).pitch(300, 2500)

    bot(7).write_analog(512)
    bot(8).write_analog(512)
    sleep(2000)
    io(9).states(6, 12)
    io(9).directions(6, 15)

bot().disconnect()