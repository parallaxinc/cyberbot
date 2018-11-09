# IR_Follow_DA.py 

# Pending firmware update 

# P11-R2k-IRLED-P20
# P9-IR detector
# P3-IR detector
# p1-R2k-IRLED-P21

setPoint = 4
errorL = 0
errorR = 0
driveL = 0
driveR = 0
kp = -8

bot(22).frequency_out(500, 1000)

while True:
    
    irL = 0
    irR = 0
    
    for da in range(512, 0, -64):
        bot(20).analog_write(da)
        bot(21).analog_write(da)
        irL += bot(9).ir_detect(11, 38000)
        irR += bot(3).ir_detect(1, 38000)
        
    for n in range(0, 5, 1):
        display.set_pixel(4, n, 0)
        display.set_pixel(3, n, 0)
        display.set_pixel(0, n, 0)
        display.set_pixel(1, n, 0)
        
    for n in range(0, irL, 1):
        if n < 5:
            display.set_pixel(4, n, 5)
        else:
            display.set_pixel(3, n-5, 5)

    for n in range(0, irR, 1):
        if n < 5:
            display.set_pixel(0, n, 5)
        else:
            display.set_pixel(1, n-5, 5)

    errorL = setPoint - irL
    errorR = setPoint - irR
    
    driveL = kp * errorL
    driveR = -kp * errorR

    bot(18).servo_speed(driveL)
    bot(19).servo_speed(driveR)