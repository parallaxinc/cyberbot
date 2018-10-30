bot(22).frequency_out(500, 1000)

while True:

    # read the phototransistors
    pL = bot(9).rc_time(1)
    pR = bot(5).rc_time(1)

    # make a "log-scale" graph by
    # turning the sensor readings into 
    # strings and counting the digits
    gL = 4 - len(str(pL * 4))
    gR = 4 - len(str(pR * 4))
    
    for y in range(0,4):
        if y <= gL:
            display.set_pixel(4, y, 9)
        else:
            display.set_pixel(4, y, 0)
        if y <= gR:
            display.set_pixel(0, y, 9)
        else:
            display.set_pixel(0, y, 0)

    # set the wheel speed variables according
    # to the normalized differential
    nDiff = round((150 * pR) / (pR + pL + 1) - 75)

    wL = 64 - nDiff
    wR = -64 - nDiff
    
    bot(18).servo_speed(wL)
    bot(19).servo_speed(wR)
