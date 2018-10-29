##################################
# IR Roaming                     #
# IR detector connected to pin 0 #
##################################

while True:
    num = bot(0).tv_remote()
    if num < 1000:
        display.scroll( str(num), 75, wait=False )
    sleep(100)