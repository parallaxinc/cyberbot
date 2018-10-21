from microbit import *
 
start = 0x07
end = 0x70
 
while True:
    display.show(Image.ARROW_W)
    if button_a.was_pressed():
        display.show(Image.SMILE)
        print("Scanning I2C bus...")
        for i in range(start, end + 1):
            try:
                i2c.read(i, 1)
            except OSError:
                pass
            else:
                print("Found:  [%s]" % hex(i))
        print("Scanning complete")
    sleep(10)
