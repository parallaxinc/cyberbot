# Navigate_FBS.py

from cyberbot import *
from group_io import *

while True:

	bot(22).tone(1000, 300)

	io(9,6).directions(15)
	sleep(1000)

	for n in range(15, -1, -1):
		io(9,6).states(n)
		dirs = io(9,6).directions(None)
		states = io(9,6).states(None)
		print("dirs = %d" % dirs)
		print("states = %d" % states)
		sleep(300)

	bot(22).tone(1500, 300)

	io(9,6).states(3)

	for n in range(15, -1, -1):
		io(9,6).directions(n)
		dirs = io(9,6).directions(None)
		states = io(9,6).states(None)
		print("dirs = %d" % dirs)
		print("states = %d" % states)
		sleep(300)

	bot(22).tone(2000, 300)

	io(9,6).states(12)
	io(9,6).directions(12)
	for n in range(1, 4, 1):
		io(9,9).directions(1)
		sleep(400)
		io(9,9).directions(0)
		sleep(400)
		io(9,8).states(1)
		sleep(400)
		io(9,8).states(0)
		sleep(400)

	io(9,8).states(0)
	bot(22).tone(2500, 300)

	bot(7).write_analog(512)
	bot(8).write_analog(512)
	sleep(2000)
	io(9,6).states(12)
	#io(9,6).directions(15)
	sleep(1000)

#bot().detach()