from cyberbot import *
from shift import *

def mcp3002_read(cs, clk, dout, din, channel, singleEnded, msbf):
	cmd = 8
	result = 0
	singleEnded &= 1
	channel &=1
	msbf &= 1
	orderIn = 3 - msbf
	cmd |= (singleEnded << 2)
	cmd |= (channel << 1)
	cmd |= (msbf << 0)
	bot(cs).write_digital(0)
	shift(din,clk).send(msbf, 5, cmd)
	result = shift(dout,clk).receive(orderIn, 10)
	bot(cs).write_digital(1)
	return result

while True:
	a1 = mcp3002_read(13, 12, 11, 10, 1, 1, 1,)
	a0 = mcp3002_read(13, 12, 11, 10, 0, 1, 1,)
	print("a0 = %d, a1 = %d" % (a0, a1))
	sleep(1000)