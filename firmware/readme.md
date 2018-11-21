# This folder contains Propeller-based firmware for the cyber:bot product.

## Using BlocklyProp
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

3a. [Open version 0.1](http://demo.blockly.parallax.com/blockly/projectlink?id=2104&key=39344de2-50c5-4bcc-afc4-0414d3de5055) on the Demo site.

3b. [Open version 0.2](http://blockly.parallax.com/blockly/projectlink?id=64207&key=5e20817a-ea20-4ee8-a178-a1ea6137dc93) on the main Blockly site.

3c. [Open version 0.3](http://demo.blockly.parallax.com/blockly/projectlink?id=2123&key=6b8fd72f-054e-4e60-9245-00b3316603c4) on the Demo site.

4. Click the green down-arrow with the bar to load the code to EEPROM.

## Using SimpleIDE

1. Make sure you have the latest version of SimpleIDE.    
   * Mac: Open SimpleIDE, click the SimpleIDE menu, and select About SimpleIDE.  
   * Windows: Open SimpleIDE, click the Help menu, and select About.  
   In either case, a banner should appear with "SimpleIDE Version 1.1.0".
   * If you do not have the latest version:
       * Close SimpleIDE.
       * Optionally, zip your existing ...Documents\SimpleIDE folder so that you have a backup that's easy to find.
       * Go to [Propeller C - Set Up SimpleIDE](http://learn.parallax.com/tutorials/language/propeller-c/propeller-c-set-simpleide), and follow the installation instruction link for your Mac or Windows OS. 
       * After installing or reinstalling SimpleIDE, run it once, and follow the prompts to let it automatically create/update your Workspace.

2. Manually update your Simple Libraries folder.  (Yes, do this, even if it just automatically updated your Workspace folder in step 1.)
   * Find and delete your Simple Libraries folder.  Its default location is ...Documents\SimpleIDE\Learn\ 
   * Here is a direct link to [Simple-Libraries-demo.zip](https://github.com/parallaxinc/Simple-Libraries/archive/demo.zip).  Download and unzip it.
   * In a file browser, find the Simple Libraries folder.  If you or your web browser unzipped it into ...Downloads, you can find it in ...Downloads\Simple-Libraries-demo\Learn\
   * Right click and copy that Simple Libraries folder.
   * Go to ...Documents\SimpleIDE\Learn\ and paste the new Simple Libraries folder into it.

3. Connect a Prop Plug as indicated in the instructions above.

4. Download and open the MicroBit Bot Firmware v0_3 project in SimpleIDE.  Here are two ways to do that.
   * In SimpleIDE, open a new project and paste in the code from [MicroBit Bot Firmware v0_3.c](https://github.com/parallaxinc/cyberbot/blob/master/firmware/MicroBit%20Bot%20Firmware%20v0_3.c)
   * Save the files in these two links [MicroBit Bot Firmware v0_3.c](https://github.com/parallaxinc/cyberbot/blob/master/firmware/MicroBit%20Bot%20Firmware%20v0_3.c) [MicroBit Bot Firmware v0_3.side](https://github.com/parallaxinc/cyberbot/blob/master/firmware/MicroBit%20Bot%20Firmware%20v0_3.side to the same folder, then open the .side file with SimpleIDE.

5. Set SimpleIDE's COM Port dropdown to your PropPlug's port.

6. Click the Load EEPROM & Run button (or select Load EEPROM & Run F11 from the Program menu).
