This folder contains the Python module (library) file for the cyber:bot product.

## Instructions for using Python code from this folder with the cyber:bot
### Set up the Mu editor
  1. Open the [Mu editor](https://codewith.mu/en/download) and set the mode to Micro:bit
  1. In the lower-right corner, click the gear
  1. Click the 'BBC Micro:bit settings' tab
  1. Check the 'Minify Python code before flashing' box

### Make the Parallax module resident on your micro:bit
> Follow the instructions below, or [watch a short video](https://photos.app.goo.gl/KTB5uVHFifFiQKn1A) to complete the process.
  1. _Power and connect_ your micro:bit to your computer
  1. Copy the **parallax.py** module to your home folder's _mu_code_ subfolder 
     * Do not use the _src_ file (un-minified, full source code) because it is too large for the micro:bit!
     * You can find the _mu_code_ subfolder location by clicking the _Load_ button in Mu and looking at the path shown in the Explorer/Finder window
  1. In Mu, click on the _Files_ button
  1. Select and drag the **parallax.py** file from the _Files on your computer:_ pane to the _Files on your micro:bit:_ pane
     * This will transmit the file to your micro:bit where it will stay resident until a future action removes/replaces it
### Import the Parallax module into your project
  1. Once all the above is done, you can write your project code or copy and paste one of the projects from the [examples folder](https://github.com/parallaxinc/cyberbot/tree/master/examples)
  1. Ensure that your project code uses the following syntax to import every class (including those of the microbit module) into your project
     ```
     from parallax import *
     ```
  1. Use ```bot().``` to access the cyber:bot API; for example:
     ```
     bot(22).frequency_out(500, 2000)
     ```
  1. Flash your code to your micro:bit/cyber:bot

## Minifying files:
An online, minimal python minifier is available here, and was written just for this repository:
[cyber:bot python minifier](http://jsfiddle.net/7pvxfurL/2/)
