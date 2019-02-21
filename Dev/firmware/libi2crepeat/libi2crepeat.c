#include "simpletools.h"
#include "i2crepeat.h"


#include "simpletools.h"                      // Include simpletools header

i2c *eeBus;                                   // I2C bus ID

int main()                                    // Main function
{
  eeBus = i2c_newbus(28,  29,   0);           // Set up I2C bus, get bus ID

  i2crepeat *i2rep = i2crepeat_master(eeBus, 5, 4);

                                              // Use eeBus to write to device
  i2c_out(eeBus, 0b1010100,                   // with I2C address 0b1010000,
          10, 2, "aBCdefg", 8);            // send address 32768 (2 bytes)
                                              // and "abc..." data (8 bytes)

//  while(i2c_busy(eeBus, 0b1010000));          // Wait for EEPROM to finish  
  pause(1000);
  char testStr[] = {0, 0, 0, 0, 0, 0, 0, 0};  // Set up test string   

                                              // Use eeBus to read from device
  i2c_in(eeBus, 0b1010100,                    // with I2C address 0b1010000,
         10, 2, testStr, 8);               // send address 32768 (2 bytes)
                                              // data in to testStr (8 bytes)

  print("testStr = %s \n", testStr);          // Display result
}














/*
unsigned char i2cAddr = 0x1d;       // I2C address of Accelerometer
unsigned char modeReg = 0x16;       // Mode register
unsigned char mode2g = 0x05;        // 2 g mode
unsigned char xRegister = 0x06;     // Device ID register
unsigned char yRegister = 0x07;     // Device ID register
unsigned char zRegister = 0x08;     // Device ID register

signed char response;               // Stores I2C responses
int x, y, z;                        // Axis measurements

int main()
{
  //i2cRepeater *i2rep;
  i2c *bus = i2c_newbus(28, 29, 0);
  //print("bus = %d\r", bus);

  i2crepeat *i2rep = i2crepeat_master(bus, 5, 4);
  //print("i2rep = %d\r", i2rep);
  //i2cRepeater *i2rep = i2crepeater_open(bus, 5, 4);

  //pause(10);
  
  i2c_out(bus, i2cAddr, modeReg, 1, &mode2g, 1);

  while(1)
  {
    i2c_in(bus, i2cAddr, xRegister, 1, &response, 1);
    x = (int) response; 
    print("x: %d", x);
    i2c_in(bus, i2cAddr, yRegister, 1, &response, 1);
    y = (int) response; 
    print(", y: %d", y);
    i2c_in(bus, i2cAddr, zRegister, 1, &response, 1);
    z = (int) response; 
    print(", z: %d\r", z);


                                                // Use eeBus to write to device
    i2c_out(bus, 0b1010000,                   // with I2C address 0b1010000,
            32768, 2, "abcdefg", 8);            // send address 32768 (2 bytes)
                                                // and "abc..." data (8 bytes)
  
    while(i2c_busy(bus, 0b1010000));          // Wait for EEPROM to finish  
  
    char testStr[] = {0, 0, 0, 0, 0, 0, 0, 0};  // Set up test string   
  
                                                // Use eeBus to read from device
    i2c_in(bus, 0b1010000,                    // with I2C address 0b1010000,
           32768, 2, testStr, 8);               // send address 32768 (2 bytes)
                                                // data in to testStr (8 bytes)
  
    print("testStr = %s \n", testStr);          // Display result

    pause(1000);
  }    
  
}



*/