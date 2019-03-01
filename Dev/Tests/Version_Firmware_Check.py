# Version_Firmware_Check.py

from cyberbot import *
from firmware_checker import *

bot(22).tone(2000, 20400)
firmware().version_info()