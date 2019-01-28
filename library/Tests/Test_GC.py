# Test_GC.py

from parallax import *
import gc

print("alloc %d" % gc.mem_alloc())
print("free %d" % gc.mem_free())

bot(22).frequency_out(300, 2000)

bot().disconnect()
