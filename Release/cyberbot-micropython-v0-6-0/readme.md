This folder contains the MicroPython modules for the cyber:bot product.

## Instructions for using MicroPython code from this folder with the cyber:bot
### Set up the Mu editor
  1. Open the [Mu editor](https://codewith.mu/en/download) and set the mode to Micro:bit
  1. In the lower-right corner, click the gear
  1. Click the 'BBC Micro:bit settings' tab
  1. Check the 'Minify Python code before flashing' box

### Make the cyberbot modules resident on your micro:bit
  1. _Power and connect_ your micro:bit to your computer
  1. Copy the **cyberbot.py** module (and any others desired) to your home folder's _mu_code_ subfolder 
     * You can find the _mu_code_ subfolder location by clicking the _Load_ button in Mu and looking at the path shown in the Explorer/Finder window
  1. In Mu, click on the _Files_ button
  1. Select and drag the **cyberbot.py** file (and any others desired) from the _Files on your computer:_ pane to the _Files on your micro:bit:_ pane
     * This will transmit the file to your micro:bit where it will stay resident until a future action removes/replaces it
### Import the cyberbot module into your project
  1. Once all the above is done, you can write your project code or copy and paste one of the projects from the cyberbot-micropython.../examples subfolder in the [Release folder](https://github.com/parallaxinc/cyberbot/tree/master/Release)
  1. Ensure that your project code uses the following syntax to import whole cyberbot module into your project
     ```
     from cyberbot import *
     ```
  1. Use ```bot().``` to access the cyber:bot API; for example:
     ```
     bot(22).frequency_out(500, 2000)
     ```
  1. Flash your code to your micro:bit/cyber:bot