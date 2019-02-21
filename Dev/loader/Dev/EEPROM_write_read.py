from microbit import *

ee_i2c_addr = 0x50
ee_mem_addr = b'\x80\x00'
data = b'ABCDEFG\r'
packet = ee_mem_addr + data

print("packet = ", packet)

# Open channel to Propeller I2C bus
pin8.write_digital(1)
sleep(1)

i2c.write(ee_i2c_addr, packet, False)
sleep(100)

data_from_ee = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
print("data_from_ee (before) = ", data_from_ee)

i2c.write(ee_i2c_addr, ee_mem_addr, False)
data_from_ee = i2c.read(ee_i2c_addr, 8, False)
print("data_from_ee (after) = ", data_from_ee)
