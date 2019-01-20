# Light_Seek_Bright.py

from parallax import *

bot(22).frequency_out(500, 1000)

while True:

    # read the phototransistors, qt stands for charge time
    bot(5).digital_write(1)
    bot(11).digital_write(1)
    qtR = bot(5).rc_time(1)
    qtL = bot(11).rc_time(1)

    # Make one normalized differential measurement
    # from R/L sensor measurements.
    nDiff = (200 * qtR) / (qtR + qtL + 1) - 100

    # Optionally scale nDiff for sharper turn repsonses.
    nDiff = (nDiff * 4) / 2
    print("qtL = %d, qtR = %d, nDiff = %d" % (qtL, qtR, nDiff))

    # Set wheel speeds according to nDiff
    # Omega looks like a lower-case w and is used in rotational
    # velocity calculations.
    if nDiff > 0:
        wL = 64 - nDiff
        wR = -64
    else:
        wL = 64
        wR = -64 - nDiff

    bot(18).servo_speed(wL)
    bot(19).servo_speed(wR)
