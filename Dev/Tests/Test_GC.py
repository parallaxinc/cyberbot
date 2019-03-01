# Test_GC.py

from cyberbot import *
import gc

print("alloc %d" % gc.mem_alloc())
print("free %d" % gc.mem_free())

bot(22).tone(2000, 300)

bot().detach()
