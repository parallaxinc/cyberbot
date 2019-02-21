from microbit import *

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

print('Enter memory address >= 32768: ')
mem_addr = repl_get_val()
print('Memory address = %d' %mem_addr)  

print('Enter value:')
value = repl_get_val()
print('value = %d' %value)  

ee_i2c_addr = 80
# mem_addr = 32768
ee_mem_addr = mem_addr.to_bytes(2, 'big')
data = value.to_bytes(4, 'little')

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
data_from_ee = i2c.read(ee_i2c_addr, 4, False)
print("data_from_ee (after) = ", data_from_ee)