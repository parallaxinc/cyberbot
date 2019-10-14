### ColorPal Firmware Update and Tests

## Setup

- Download & unzip  "ColorPal Firmware and Tests (Alpha).zip".
- Connect the cyber:bot to your computer with USB.  Make sure batteries are good, set PWR to 1..
- Go to https://python.microbit.org/v/beta
- Click the Connect button, select the micro:bit, and click Connect.
- Open and print "ColorPal Test Colors.pdf" with a color printer or at least obtain red, green, blue, white and black things to test.
- Connect the ColorPal: 
     - P6 to Wh, 5V to Rd, and GND to Bk. 
## cyber:bot board Firmware Update
- Click the Load/Save button.
- Click the "Or browse for a file" link in the Load category.
- Browse into the folder you unzipped (not the zip, the folder), and and open "Cyber-Bot-Board-Firmware-v01.00.06.hex"
NOTE: I also included v10.00.02 in case you want to go back to the original non-ColorPal version.  For this part, make sure to open the 06 version.
- Click Flash
- Click Open Serial
- Click the Send CTRL-C for REPL button.
- Click the Send CTRL-D to reset button. IMPORTANT: Now, click the terminal.  Otherwise, it won't catch your keystrokes.  
- Press your keyboard's Y key to update, and wait for it to count to 149.
- IMPORTANT: Set PWR to 0, then back to 1.  This loads the firmware that was transferred to EEPROM into the Propeller.  
- Check for a message confirming that the firmware is up-to-date.
- Press the N key to exit the application.
- Click Close Serial
## First Test
- In the online editor, use Load/Save, then click "Or browse for a file" and open "ColorPal_Test.hex" from the folder.
- Flash, then Open Serial.
- Make notes of the r, g, and b values for white, black, red, green, and blue.  Also, verify that each one gave you a set of 3 values that can't be confused with the other sets of three values.  For example, here are my values.  Yours will probably differ depending on printer or other color samples.  The main thing is you want to be sure you could tell them apart based on the readings.  (I haven't tried a color inkjet, the colors might or might not be more difficult to discern.)  Also, blue vs. green PCBs weren't quite as clearly different either.  
     White   250  230   400
     Red     220   35    60
     Green    50   100   70
     Cyan     30   100  300
     Black    30    25   40
     None      0     0    0
## Second Test
- Open ColorPal_Color Enumerator.hex
- Update the cyan, red, green and white values to match the ones you noted.
- Flash and then click Open serial
- Verify that it can recognize those colors
## Third Test
- I did this one to verify that the ColorPal can coexist with the bot and another sensor in an application.
- Add a forward facing Ping))) to P16 (or an I/O pin of your choice so long as you update it in the script).   
- Flash, and set PWR to 1.
- Hold color swatches up against the ColorPal for motion (or no motion if Ping detects an object closer than 10 cm):  cyan = forward, red = left, green = right, white = backward.
