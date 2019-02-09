# Test_GC.py

from cyberbot import *
import gc

print("alloc %d" % gc.mem_alloc())
print("free %d" % gc.mem_free())

bot(22).pitch(300, 2000)

bot().disconnect()
