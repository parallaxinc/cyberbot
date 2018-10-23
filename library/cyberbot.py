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

    def __init__(self, p, a=0x5D):
        self.addr = a
        self.pin = p
        while True:
            try:
                i2c.read(a, 1)
            except OSError:
                pass
            else:
                break

    def send_c(self, c, p=0, s=0, d=None, f=None):
        bb = bytes([1, self.pin, p, s])
        if d is not None:
            bb = bb + d.to_bytes(4, 'little')
        if f is not None:
            bb = bb + f.to_bytes(4, 'little')
        i2c.write(self.addr, bb)
        i2c.write(self.addr, bytes([0, c]))
        s = b'\x01'
        while s != b'\x00':
            i2c.write(self.addr, b'\x00')
            s = i2c.read(self.addr, 1)

    def read_r(self):
        i2c.write(self.addr, b'\x18')
        r = i2c.read(self.addr, 4)
        return int.from_bytes(r, 'little')

    def digital_write(self, s):
        if s > 1 or s < 0:
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
            raise ValueError('start pin > end pin!')
        elif sp == self.pin and s is None:
            return self.digitalRead()
        elif sp == self.pin:
            self.digital_write(s & 1)
        elif s is None:
            self.send_c(8, sp)
            return self.read_r()
        else:
            self.send_c(7, sp, s)

    def directions(self, ep, sp, d):
        self.pin = ep
        if sp > self.pin:
            raise ValueError('start pin > end pin!')
        elif d is None:
            self.send_c(6, sp)
            return self.r()
        else:
            self.send_c(5, sp, d)

    def pulse_out(self, d):
        self.send_c(11, 0, 0, d)

    def pulse_in(self, s):
        self.send_c(10, 0, s)
        return self.read_r()

    def pulse_count(self, d):
        self.send_c(12, 0, 0, d)
        return self.read_r()

    def rc_time(self, s):
        self.send_c(16, 0, s)
        return self.read_r()

    def frequency_out(self, d, f):
        self.send_c(13, 0, 0, d, f)

    def ir_detect(self, lp, f):
        self.send_c(31, lp, 0, f)
        return self.read_r()

    def servo_angle(self, v):
        self.send_c(24, 0, 0, v)

    def servo_speed(self, v):
        self.send_c(25, 0, 0, v)

    def servo_set(self, v):
        self.send_c(26, 0, 0, v)

    def servo_ramping(self, v):
        self.send_c(27, 0, 0, v)

    def servo_disable(self):
        self.send_c(28)

    def ping_distance(self, u=None):
        self.send_c(29)
        d = self.read_r()
        if u is None:
            return d
        elif u == 'in':
            return d / 148
        else:
            return d / 58

    def tv_remote(self):
        self.send_c(30)
        return self.read_r()

##########################
# User code/test harness #
##########################

# bot_pin(22).frequency_out(500, 1000)
# bot_pin(18).servo_speed(50)
# bot_pin(19).servo_speed(-50)

while True:
    irR = bot_pin(1).ir_detect(3, 39000)
    irL = bot_pin(11).ir_detect(9, 39000)
    
    bot_pin(7).digital_write(irR)
    bot_pin(8).digital_write(irL)

    # bot_pin(21).digital_write(3)
    # sleep(250)
    # bot_pin(21).digital_write(3)
    # sleep(250)
    # t = bot_pin(1).digital_read()
    # if t == 0:
    #     display.show(Image.HAPPY)
    # else:
    #     display.show(Image.SAD)
