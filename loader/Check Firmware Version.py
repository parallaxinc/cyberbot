# Check Firmware Version.py

from cyberbot import *

def version_info():
    bot().send_c(98)
    v = bot().read_r()
    p=v%100
    mi=((v%10000)-p)/100
    ma=((v%1000000)-mi-p)/10000
    print("Firmware: v%d.%d.%d" %(ma, mi, p))

bot(22).pitch(200, 2000)
version_info()