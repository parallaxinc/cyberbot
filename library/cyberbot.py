from microbit import *


############################################################
# STILL HERE BECAUSE I HAVEN’T WRITTEN THESE FUNCTIONS YET #
############################################################
SHIFTIN = 17
SHIFTOUT = 18
SEROUT = 19
SERIN = 20


##############################
# The cyber:bot class itself #
##############################

class bot_pin():

    def __init__(self, bPin, i2cAddress=0x5D):
        self.addr = i2cAddress
        self.pin = bPin
        while True:
            try:
                i2c.read(i2cAddress, 1)
            except OSError:
                pass
            else:
                break

    def send_command(self, c, cmd=None):
        i2c.write(self.addr, bytes([1, self.pin]))
        if cmd is not None:
            i2c.write(self.addr, cmd)
        i2c.write(self.addr, bytes([0, c]))
        s = b'\x01'
        while s != b'\x00':
            i2c.write(self.addr, b'\x00')
            s = i2c.read(self.addr, 1)

    def read_result(self, s=None):
        if s is None:
            i2c.write(self.addr, b'\x18')
            r = i2c.read(self.addr, 4)
            return int.from_bytes(r, 'little')
        else:
            i2c.write(self.addr, b'\x1C')
            r = i2c.read(self.addr, s)
            return r.decode()

    def digital_write(self, s):
        if s > 1:
            s = 4
        elif s == 0:
            s = 2
        self.send_command(s)

    def digital_read(self):
        self.send_command(3)
        return self.read_result()

    def states(self, ep, sp, s):
        self.pin = ep
        if sp > self.pin:
            raise ValueError('start pin is higher than end pin!')
        elif sp == self.pin and s is None:
            return self.digitalRead()
        elif sp == self.pin:
            self.digital_write(s & 1)
        elif s is None:
            self.send_command(8, bytes([2, sp]))
            return self.read_result()
        else:
            self.send_command(7, bytes([2, sp]) + b'\x00' + 
                              s.to_bytes(4, 'little'))

    def directions(self, ep, sp, d):
        self.pin = ep
        if sp > self.pin:
            raise ValueError('start pin is higher than end pin!')
        elif d is None:
            self.send_command(6, bytes([2, sp]))
            return self.read_result()
        else:
            self.send_command(5, bytes([2, sp]) + b'\x00' + 
                              d.to_bytes(4, 'little'))
            
    def pulse_out(self, d):
        self.send_command(11, b'\x04' + d.to_bytes(4, 'little'))

    def pulse_in(self, s):
        self.send_command(10, bytes([3, s]))
        return self.read_result()

    def pulse_count(self, d):
        self.send_command(12, b'\x04' + d.to_bytes(4, 'little'))
        return self.read_result()

    def rc_time(self, s):
        self.send_command(16, bytes([3, s]))
        return self.read_result()

    def frequency_out(self, d, f):
        self.send_command(13, b'\x04' + d.to_bytes(4, 'little') + 
                          f.to_bytes(4, 'little'))

    def servo_angle(self, v):
        self.send_command(24, b'\x04' + v.to_bytes(4, 'little'))

    def servo_speed(self, v):
        self.send_command(25, b'\x04' + v.to_bytes(4, 'little'))

    def servo_set(self, v):
        self.send_command(26, b'\x04' + v.to_bytes(4, 'little'))

    def servo_ramping(self, v):
        self.send_command(27, b'\x04' + v.to_bytes(4, 'little'))

    def servo_disable(self):
        self.send_command(28)

    def ping_distance(self, unit=None):
        self.send_command(29)
        d = self.read_result()
        if unit is None:
            return d
        elif unit == 'in':
            return d / 148
        else:
            return d / 58

    def tv_remote(self):
        self.send_command(30)
        return self.read_result()

##########################
# User code/test harness #
##########################

bot_pin(18).servo_speed(50)
bot_pin(19).servo_speed(-50)

while True:
    bot_pin(21).digital_write(0)
    sleep(500)
    bot_pin(21).digital_write(1)
    sleep(500)
    t = bot_pin(1).digital_read()
    if t == 0:
        display.show(Image.HAPPY)
    else:
        display.show(Image.SAD)
