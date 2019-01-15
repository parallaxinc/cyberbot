# Navigate_FBS.py

from parallax import *

display.off()
ad4 = pin4.read_analog()
display.on()

print('ad4 = %d' % ad4)

v = ad4 * 3.246 / 1024    # Convert to volts

# Undo down-scaling that circuit on board performs for safe measurements over 3.3 V
v = v * (64.9 / 10.0)   

print("Batery volage: %f" % v)
