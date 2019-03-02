# load_firmware_102.py
# Use Mu editor to copy cbfw102a.bin and cbfw102b.bin to the micro:bit module's
# file system, then run this.  Open REPL, CTRL+D and follow the prompts.
# When "Done!", disconnect programming cable and PWR 0
# Reconnect, PWR 1, and run Check Firmware Version.py

from microbit import *
import os

def repl_get_val():
    c = None
    val = b''
    while True:
        c = uart.read()
        if c is not None:
            if c == b'\r':
                break
            val += c
            c = None
    return int(val)

print("To start firmware update, type 102 and press Enter:")

val = 0
while val != 102:
    val = repl_get_val()

print("Please wait about 20 s...")

# print(os.listdir())

ee_i2c_addr = 80
ee_mem_addr = 0
mem_addr = 0

pin8.write_digital(1)
sleep(1)

f = open("cbfw102a.bin", "rb")

buf = bytearray(128)

for m in range(0, 72):
	f.readinto(buf, 128)
	ee_mem_addr = mem_addr.to_bytes(2, 'big')
	packet = ee_mem_addr + buf
	i2c.write(ee_i2c_addr, packet, False)
	mem_addr += 128
	sleep(100)

f.close()

f = open("cbfw102b.bin", "rb")

buf = bytearray(128)

for m in range(72, 144):
	f.readinto(buf, 128)
	ee_mem_addr = mem_addr.to_bytes(2, 'big')
	packet = ee_mem_addr + buf
	i2c.write(ee_i2c_addr, packet, False)
	mem_addr += 128
	sleep(100)

buf2 = bytearray(20)

f.readinto(buf2, 20)
mem_addr = 0x4800
ee_mem_addr = mem_addr.to_bytes(2, 'big')
packet2 = ee_mem_addr + buf2
i2c.write(ee_i2c_addr, packet2, False)

sleep(100)
f.close()

sleep(100)

print("Done!")

# for mem_addr in range(0, 0x4880, 128):
#	 print("mem_addr = %d" % mem_addr)
#	 ee_mem_addr = mem_addr.to_bytes(2, 'big')
#	 i2c.write(ee_i2c_addr, ee_mem_addr, False)
#	 j = i2c.read(ee_i2c_addr, 128, False)
#	 for n in j: print("%x" % n)

