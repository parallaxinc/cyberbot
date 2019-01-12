# IR_Distance_Test_F.py

from parallax import *

bot(22).frequency_out(500, 1000)

while True:
    
    irL = 0
    irR = 0
    
    for f in range(38000, 43000, 1000):
        irR += bot(13).ir_detect(14, f)
        irL += bot(2).ir_detect(1, f)

    for n in range(0, 5, 1):
        display.set_pixel(4, n, 0)
        display.set_pixel(0, n, 0)
        
    for n in range(0, irL, 1):
        display.set_pixel(4, n, 5)
    for n in range(0, irR, 1):
        display.set_pixel(0, n, 5)
        
    sleep(20)