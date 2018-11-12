###################################
#   Push Ping Example             #
#   Requires v0.3 firmware/lib    #
###################################

bot(22).frequency_out(500, 1000)

setPoint = 32
kP = -7

while True:
    distance = bot(10).ping_distance('cm')
    
    errorVal = setPoint - distance
    speed = kP * errorVal
    
    if speed > 0:
        display.show(Image("00000:"
            "00000:"
            "99999:"
            "09090:"
            "00900"))
    elif speed < 0:
        display.show(Image("00900:"
            "09090:"
            "99999:"
            "00000:"
            "00000"))
    else:
        display.show(Image.DIAMOND)

    bot(18).servo_speed(speed, 19, speed)
