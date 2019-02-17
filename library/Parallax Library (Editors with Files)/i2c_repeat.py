from cyberbot import *

class i2c_repeat():
    # def __init__(self,p=0):
    #     self.pin=p
    def pins(p,q):
        bot().send_c(40,0,0,p,q)
        # bot(self.pin).send_c(40,q)
