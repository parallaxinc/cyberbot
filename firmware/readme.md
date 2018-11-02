# This folder contains Propeller-based firmware for the cyber:bot product.

## Using [BlocklyProp Demo](http://demo.blockly.parallax.com)
### Make sure you have an account and that the appropriate client/launcher software is installed on your computer
[Getting Started with BlocklyProp](http://learn.parallax.com/tutorials/language/blocklyprop/getting-started-blocklyprop)

### Open the project and load it to your cyber:bot

1. Connect the cyber:bot board to a 6 to 24 VDC power supply, and turn on the power switch (position 1 or 2)

2. Connect the Prop Plug to the computer, through a USB cable, and connect to the cyber:bot board
    * If you have an adapter, connect the Prop Plug, the adapter, and the cyber:bot board using [this orientation](https://github.com/parallaxinc/cyberbot/blob/master/firmware/Adapter.jpg)
    * If you don't have an adapter, use the same header, but use jumper wires to make the following connections:
      * VSS - The pin closest to the center of the micro:bit board
      * !RES - The pin immediately to the left of VSS
      * <TX - The pin immediately below *and* to the left of VSS
      * \>RX - The pin immediately below VSS

3a. [Open the project](http://demo.blockly.parallax.com/blockly/projectlink?id=2104&key=39344de2-50c5-4bcc-afc4-0414d3de5055) - version 0.1 (Demo).

3b. [Open the project](http://blockly.parallax.com/blockly/projectlink?id=64207&key=5e20817a-ea20-4ee8-a178-a1ea6137dc93) - version 0.2 (Main Blockly Site - multiple refreshes may be required to make it appear until the site is updated ~Nov. 3, 2018)

4. Click the green down-arrow with the bar to load the code to EEPROM.
