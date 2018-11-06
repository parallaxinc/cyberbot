##########################
# IR Follow              #
##########################

# DOES NOT WORK WITH 11/1 FIRMWARE & LIBRARY
# Developed & tested with 10/25 firmwrae and library.
# Search & replace bot_pin with bot for next iteration, 
# assuming command times get reduced from 30 ms back to 4 ms.

setPoint = 3
errorL = 0
errorR = 0
driveL = 0
driveR = 0
kp = -18

bot_pin(22).frequency_out(500, 1000)

while True:
    
    irL = 0
    irR = 0
    
    for f in range(38000, 43000, 1000):
        irL += bot_pin(9).ir_detect(11, f)

    for f in range(38000, 43000, 1000):
        irR += bot_pin(3).ir_detect(1, f)

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

    bot_pin(18).servo_speed(driveL)
    bot_pin(19).servo_speed(driveR)
        
    # sleep(20)