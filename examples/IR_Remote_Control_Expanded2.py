# IR_Remote_Control_Expanded2.py
# Code adjusted to make room for frequency_out.

from parallax import *

speedL = 0
speedR = 0
img = Image.HAPPY

bot(22).frequency_out(300, 2000)

while True:
    num = bot(2).tv_remote()

    if num == 1:
        speedL=0
        speedR=-75
        img=Image.ARROW_SE
    elif num == 2:
        speedL=75
        speedR=-75
        img=Image.ARROW_S
    elif num == 3:
        speedL=75
        speedR=0
        img=Image.ARROW_SW
    elif num == 4:
        speedL=-75
        speedR=-75
        img=Image.ARROW_E
    elif num == 5:
        speedL=0
        speedR=0
        img=Image.HAPPY
    elif num == 6:
        speedL=75
        speedR=75
        img=Image.ARROW_W
    elif num == 7:
        speedL=0
        speedR=75
        img=Image.ARROW_NE
    elif num == 8:
        speedL=-75
        speedR=75
        img=Image.ARROW_N
    elif num == 9:
        speedL=-75
        speedR=0
        img=Image.ARROW_NW

    display.show(img)
    bot(18).servo_speed(speedL)
    bot(19).servo_speed(speedR)
	