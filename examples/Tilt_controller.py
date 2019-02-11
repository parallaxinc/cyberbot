# Add your Python code here. E.g.
from microbit import *
import radio

radio.on()

while True:
    reading_x = accelerometer.get_x()
    reading_y = accelerometer.get_y()
    stop = 0
    
    if reading_y < -250:
        radio.send("forward")
    if reading_x < -250:
        radio.send("left")
    if reading_x > 250:
        radio.send("right")
    if reading_y > 250:
        radio.send("back")
    if (reading_y > -250 and reading_y < 250) and (reading_x > -250 and reading_x < 250):
        radio.send("stop")

    display.clear()
    
