# Navigate_FBS.py

from parallax import *

bot(22).frequency_out(300, 2000)

display.off()
ad4 = pin4.read_analog()
display.on()

print('ad4 = %d' % ad4)

# The miro:bit supply has a low voltage diode for protection,
# so it's A/D supply is 3.3 V - diode drop.
v = ad4 * (3.3 - 0.090) / 1024    # Convert to volts

# Undo down-scaling that circuit on board performs for safe
# measurements over 3.3 V
v = v * (64.9 / 10.0)

print("Batery voltage: %f" % v)
display.show("Bat V: %2f" % v)

sleep(100)

bot(18).servo_speed(120)
bot(19).servo_speed(-120)
sleep(700)
bot(18).servo_speed(-120)
bot(19).servo_speed(120)
sleep(700)
bot(18).servo_speed(0)
bot(19).servo_speed(0)
sleep(1000)