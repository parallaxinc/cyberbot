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

    def i2by(self, c, d, f=None):
        bb = c.to_bytes(1, 'big') + d.to_bytes(4, 'little')
        if f is not None:
            bb = bb + f.to_bytes(4, 'little')
        return bb
        
    def send_c(self, c, cmd=None):
        i2c.write(self.addr, bytes([1, self.pin]))
        if cmd is not None:
            i2c.write(self.addr, cmd)
        i2c.write(self.addr, bytes([0, c]))
        s = b'\x01'
        while s != b'\x00':
            i2c.write(self.addr, b'\x00')
            s = i2c.read(self.addr, 1)

    def read_r(self, s=None):
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
        self.send_c(s)

    def digital_read(self):
        self.send_c(3)
        return self.read_r()

    def states(self, ep, sp, s):
        self.pin = ep
        if sp > self.pin:
            raise ValueError('start pin is higher than end pin!')
        elif sp == self.pin and s is None:
            return self.digitalRead()
        elif sp == self.pin:
            self.digital_write(s & 1)
        elif s is None:
            self.send_c(8, bytes([2, sp]))
            return self.read_r()
        else:
            self.send_c(7, bytes([2, sp]) + self.i2by(0, s))

    def directions(self, ep, sp, d):
        self.pin = ep
        if sp > self.pin:
            raise ValueError('start pin is higher than end pin!')
        elif d is None:
            self.send_c(6, bytes([2, sp]))
            return self.r()
        else:
            self.send_c(5, bytes([2, sp]) + self.i2by(0, d))
            
    def pulse_out(self, d):
        self.send_c(11, self.i2by(4, d))

    def pulse_in(self, s):
        self.send_c(10, bytes([3, s]))
        return self.read_r()

    def pulse_count(self, d):
        self.send_c(12, self.i2by(4, d))
        return self.read_r()

    def rc_time(self, s):
        self.send_c(16, bytes([3, s]))
        return self.read_r()

    def frequency_out(self, d, f):
        self.send_c(13, self.i2by(4, d, f))

    def servo_angle(self, v):
        self.send_c(24, self.i2by(4, v))

    def servo_speed(self, v):
        self.send_c(25, self.i2by(4, v))

    def servo_set(self, v):
        self.send_c(26, self.i2by(4, v))

    def servo_ramping(self, v):
        self.send_c(27, self.i2by(4, v))

    def servo_disable(self):
        self.send_c(28)

    def ping_distance(self, unit=None):
        self.send_c(29)
        d = self.read_r()
        if unit is None:
            return d
        elif unit == 'in':
            return d / 148
        else:
            return d / 58

    def tv_remote(self):
        self.send_c(30)
        return self.read_r()

##########################
# User code/test harness #
##########################

bot_pin(22).frequency_out(1000, 1000)
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
