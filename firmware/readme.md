# This folder contains Propeller-based firmware for the cyber:bot product.

## Before updating:

1. If you do not have propeller-load, download it from one of the following links:

    * [Linux](https://github.com/parallaxinc/BlocklyPropClient/raw/master/propeller-tools/linux/propeller-load)
    
    * [Apple OS X](https://github.com/parallaxinc/BlocklyPropClient/raw/master/propeller-tools/mac/propeller-load)
    
    * [Microsoft Windows](https://github.com/parallaxinc/BlocklyPropClient/raw/master/propeller-tools/windows/propeller-load.exe)

2. If you are using Linux or OS X, be sure to mark the file as executable

3. If you are using Microsoft Windows, and have not previously installed the FTDI driver, download and install the driver from the [FTDI USB Drivers for Windows](https://www.parallax.com/downloads/parallax-ftdi-usb-drivers-windows) page.

## Update instructions:

1. Download the desired firmware release (a '.binary' file)

2. Connect the cyber:bot board to a 6 to 24 VDC power supply, and turn on the power switch (position 1 or 2)

3. Connect the Prop Plug to the computer, through a USB cable, and connect to the cyber:bot board

    * If you have an adapter, connect the Prop Plug, the adapter, and the cyber:bot board using [this orientation](https://github.com/parallaxinc/cyberbot/blob/master/firmware/Adapter.jpg)
    
    * If you don't have an adapter, use the same header, but use jumper wires to make the following connections:
    
      * VSS - The pin closest to the center of the micro:bit board
      
      * !RES - The pin immediately to the left of VSS
      
      * <TX - The pin immediately below *and* to the left of VSS
      
      * \>RX - The pin immediately below VSS

2. Run propeller-load, with the `-e` argument, followed by the name of firmware release

    * In widows, the command will look something like this:
      
      `propeller-load.exe -e firmware_release.binary`
      
    * In Linux or OS X, it will look something like this:
    
      `./propeller-load -e firmware_release.binary`
