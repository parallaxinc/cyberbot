# Version_Firmware_Check.py

# Setup
#
#   If your editor has a Files feature, use it to copy all .py files from:
#	  Parallax Library (Editors with Files)
#   to your micro:bit module's file system.

from cyberbot import *
from firmware_checker import *

bot(22).pitch(200, 2000)
firmware().version_info()