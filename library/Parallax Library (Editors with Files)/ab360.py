# ab360.py v_0_3_9
from cyberbot import *
class drive():
    def __init__(self,p=0):
        self.pin=p
    def connect():
        bot().send_c(61)
    def speed(l,r):
        bot().send_c(62,0,0,l,r)
    def goto(l,r):
        bot().send_c(63,0,0,l,r)
    def set_acceleration(l,r):
        bot().send_c(64,0,0,l,r)