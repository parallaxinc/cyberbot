from cyberbot import *
from i2c_repeat import *

# ee_i2c_addr = 0x50
ee_i2c_addr = 0x54
# ee_mem_addr = b'\x80\x00'
ee_mem_addr = b'\x00\x80'
data = b'Abcdef1\r'
packet = ee_mem_addr + data

bot(22).pitch(200, 2000)

# bot().send_c(40,0,0,5,4)
i2c_repeat(5,4).connect()

while True:
    sleep(100)

    print("packet = ", packet)

    # Open channel to Propeller I2C bus
    # pin8.write_digital(1)
    sleep(1)

    i2c.write(ee_i2c_addr, packet, False)
    sleep(100)

    data_from_ee = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    print("data_from_ee (before) = ", data_from_ee)

    i2c.write(ee_i2c_addr, ee_mem_addr, False)
    data_from_ee = i2c.read(ee_i2c_addr, 8, False)
    print("data_from_ee (after) = ", data_from_ee)

    # bot(22).pitch(200, 1000)
    sleep(1000)

bot().disconnect()