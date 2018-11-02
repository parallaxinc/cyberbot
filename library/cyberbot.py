from microbit import *

#################################################
# The cyber:bot class                           #
#################################################
#  Version 0.2 - not compatible with firmware   #
#  below version 0.2!                           #
#################################################
#  NOTE - this now contains heavy commenting.   #
#         use the mu editor, then click the     #
#         gear in the lower-right corner, then  #
#         the micro:bit settings tab, then      #
#         select [Minify Python...] to ensure   #
#         memory isn't overflowed.              #
#         Otherwise, delete all comments before #
#         flashing to the micro:bit.            #
#################################################

class bot():

    def __init__(self, p, a=0x5D):
        self.addr = a
        self.pin = p
        while True:
            try:
                i2c.read(a, 1)
            except OSError:
                pass
            else:
                i2c.write(a, bytes([0, 99]))
                sleep(10)     # CRITICAL - do not adjust    
                pin8.write_digital(1)
                sleep(10)     # CRITICAL - do not adjust
                while True:
                    try:
                        i2c.read(a, 1)
                    except OSError:
                        pass
                    else:
                        break
                break

    # Send data to the Propeller via i2c
    #   self - allows self.pin and self.addr to be retrieved
    #   c - command code, defined as constants in cyberbot firmware
    #   p - optional|pin 2 (usually start pin, pin 1 is end pin)
    #   s - optional|state/direction (bit for 1 pin or byte for multiple pins)
    #   d - optional|argument 1
    #   f - optional|argument 2
    def send_c(self, c, p=0, s=0, d=None, f=None):
        a = bytes([1, self.pin, p, s])
        if d is not None:
            a = a + d.to_bytes(4, 'little')
        if f is not None:
            a = a + f.to_bytes(4, 'little')
        i2c.write(self.addr, a)
        i2c.write(self.addr, bytes([0, c]))
        c = b'\x01'
        while c != b'\x00':
            i2c.write(self.addr, b'\x00')
            c = i2c.read(self.addr, 1)

    # Retrieve return value data to the Propeller via i2c
    #   self - allows self.addr to be retrieved
    def read_r(self):
        i2c.write(self.addr, b'\x18')
        r = i2c.read(self.addr, 4)
        return int.from_bytes(r, 'little')

    # Set a pin to output a specified state
    #   self - allows self.pin to be retrieved
    #   s - state to set pin to.  0=low, 1=high, <0||>1=toggle
    def digital_write(self, s):
        if s > 1 or s < 0:
            s = 4
        elif s == 0:
            s = 2
        self.send_c(s)
        
    # Set a pin to PWM at a specified duty cycle
    #   self - allows self.pin to be retrieved
    #   f - duty cycle (range = 0|off to 1023|full)
    #   c - optional|channel of PWM to use (0|default or 1)
    #       ignored if pin is 20 or 21
    def analog_write(self, f, c=0):
        self.send_c(32, c, 0, f)

    # Read the digital state of a pin
    #   self - allows self.pin to be retrieved
    def digital_read(self):
        self.send_c(3)
        return self.read_r()

    # Get or set the digital states of the specified pins
    #   self - allows self.pin (end pin) to be retrieved
    #   p - start pin
    #   s - states, binary value to set (output), None to get (input)
    def states(self, p, s):
        if p > self.pin:
            raise ValueError('start pin > end pin!')
        elif self.pin - p > 8:
            raise ValueError('more than 8 pins selected!')
        elif p == self.pin and s is None:
            return self.digitalRead()
        elif p == self.pin:
            self.digital_write(s & 1)
        elif s is None:
            self.send_c(8, p)
            return self.read_r()
        else:
            self.send_c(7, p, s)

    # Get or set the directions of the specified pins
    #   self - allows self.pin (end pin) to be retrieved
    #   p - start pin
    #   s - states, binary value to set (output), None to get (input)
    def directions(self, p, d):
        if p > self.pin:
            raise ValueError('start pin > end pin!')
        elif self.pin - p > 8:
            raise ValueError('more than 8 pins selected!')
        elif d is None:
            self.send_c(6, p)
            return self.r()
        else:
            self.send_c(5, p, d)

    # Read the values of a set of QTI sensors on specified consequtive pins
    #   self - allows self.pin (end pin) to be retrieved
    #   p - start pin
    #   d - optional|duration of discharge time (default=230us)
    def qti(self, p, d=None):
        if p > self.pin:
            raise ValueError('start pin > end pin!')
        elif self.pin - p > 8:
            raise ValueError('more than 8 pins selected!')
        else:
            self.send_c(33, p, 0, d)
            return self.read_r()
            
    # Send a pulse of a specified width
    #   self - allows self.pin to be retrieved
    #   d - duration of pulse in microseconds
    def pulse_out(self, d):
        self.send_c(11, 0, 0, d)

    # Read the duraction on an incoming high or low a pulse
    #   self - allows self.pin to be retrieved
    #   s - state of pulse (0=low, 1=high) to read
    def pulse_in(self, s):
        self.send_c(10, 0, s)
        return self.read_r()

    # Count low-to-high (?) transitions for a specified duration of time
    #   self - allows self.pin to be retrieved
    #   d - duration in milliseconds
    def pulse_count(self, d):
        self.send_c(12, 0, 0, d)
        return self.read_r()

    # Charge/discharge a device and then measure its discharge/charge time
    #   self - allows self.pin to be retrieved
    #   s - measure the 1=charge or 0=discharge time
    #   d - optional|time to drive pin high or low in us (default is 1000us)
    #   f - optional|PWM duty (0-1023) to charging with (default is 1023|100%),
    #       uses a PWM channel
    #   c - optional|channel of PWM to use (0|default or 1)
    def rc_time(self, s, d=None, f=None, c=0):
        self.send_c(16, c, s, d, f)
        return self.read_r()

    # Send a frequency out a pin 
    #  NOTE - this is a blocking function
    #   self - allows self.pin to be retrieved
    #   d - duration of output in ms
    #   f - frequency to output
    def frequency_out(self, d, f):
        self.send_c(13, 0, 0, d, f)

    # Pulses an LED with the specified frequncy, then reads 
    # if the reflection was detected 
    #   self - allows self.pin (pin 1 - IR detector) to be retrieved
    #   p - pin 2 (LED)
    #   f - frequency to output to LED
    def ir_detect(self, p, f):
        self.send_c(31, p, 0, f)
        return self.read_r()

    # Set a servo to the specified angle in 10ths of degrees 
    #   self - allows self.pin to be retrieved
    #   v - angle to set servo to (0 to 1800)
    def servo_angle(self, v):
        self.send_c(24, 0, 0, v)

    # Set a CR servo to the specified speed
    #  NOTE - speeds are NOT linear
    #   self - allows self.pin to be retrieved
    #   v - speed to set servo to (-100 to 100 is approx. linear range)
    def servo_speed(self, v):
        self.send_c(25, 0, 0, v)

    # Send a servo pulse of the specified width in us
    #   self - allows self.pin to be retrieved
    #   v - pulse width (1500 = center|90deg)
    def servo_set(self, v):
        self.send_c(26, 0, 0, v)

    # Set a maximum rate of change for servo commands
    #   self - allows self.pin to be retrieved
    #   v - ramping maximum (lower=sluggish, higher=snappy)
    def servo_ramping(self, v):
        self.send_c(27, 0, 0, v)

    # Stop sending servo pulses to the specified pin
    #   self - allows self.pin to be retrieved
    def servo_disable(self):
        self.send_c(28)

    # Read a ping sensor
    #   self - allows self.pin to be retrieved
    #   u - optional|unit of measurement (default=us, 'in'=inches, 'cm'=cm)
    def ping_distance(self, u=None):
        self.send_c(29)
        d = self.read_r()
        if u is None:
            return d
        elif u == 'in':
            return d / 148
        else:
            return d / 58

    # Read a Sony remote code using an IR detector
    #  NOTE - timeout is 70ms
    #   self - allows self.pin to be retrieved
    #   returns - button code | -1 if no button pressed
    def tv_remote(self):
        self.send_c(30)
        return self.read_r()
