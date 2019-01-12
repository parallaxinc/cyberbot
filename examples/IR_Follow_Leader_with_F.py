# IR_Follow_Leader_with_F.py 

from parallax import *

setPoint = 3
errorL = 0
errorR = 0
driveL = 0
driveR = 0
kp = -18

bot(22).frequency_out(500, 1000)

while True:
    
    irL = 0
    irR = 0
    
    for f in range(38000, 43000, 1000):
        irL += bot(13).ir_detect(14, f)
        irR += bot(2).ir_detect(1, f)

    for n in range(0, 5, 1):
        display.set_pixel(4, n, 0)
        display.set_pixel(0, n, 0)
        
    for n in range(0, irL, 1):
        display.set_pixel(4, n, 5)
    for n in range(0, irR, 1):
        display.set_pixel(0, n, 5)
        
    errorL = setPoint - irL
    errorR = setPoint - irR
    
    driveL = kp * errorL
    driveR = -kp * errorR

    bot(18).servo_speed(driveL)
    bot(19).servo_speed(driveR)
        
    # sleep(20)