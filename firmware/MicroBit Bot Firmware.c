/*

  MicroBit Bot Firmware.side

  Propeller firmware mockup as I2C slave I/O expander.
*/


#include "simpletools.h"
#include "simplei2c.h"
#include "i2cslave.h"
#include "servo.h"
#include "ping.h"
#include "sirc.h"
//#include "fdserial.h"

#define COMMAND 0
#define PIN1 1
#define PIN2 2
#define STATE 3
#define ARG1 4
#define ARG2 8
#define ARG3 12
#define ARG4 16
#define ARG5 20
#define RETVAL 24
#define STRBUF 28

#define HIGH 1
#define LOW 2
#define INPUT 3
#define TOGGLE 4
#define SETDIRS 5
#define GETDIRS 6
#define SETSTATES 7
#define GETSTATES 8

#define PAUSE 9
#define PULSIN 10
#define PULSOUT 11
#define COUNT 12
#define FREQOUT 13
#define RCTIME 16

#define SHIFTIN 17
#define SHIFTOUT 18
#define SEROUT 19
#define SERIN 20

#define SERVO_ANGLE 24
#define SERVO_SPEED 25
#define SERVO_SET 26
#define SERVO_SETRAMP 27
#define SERVO_DISABLE 28

#define PING_ECHO 29
#define SIRC 30

#define UART_INIT 40
#define UART_RX_LEN 41
#define UART_READ 42
#define UART_WRITE 46

i2c *mbBusM;
i2cslave *mbBusS;
static char *reg;

/*
int pinMap[] = {
  0,    //  0
  1,    //  1
  2,    //  2
  3,    //  3
  4,    //  4
  5,    //  5
  6,    //  6
  7,    //  7
  8,    //  8
  9,    //  9
  10,   //  10
  11,   //  11
  12,   //  12
  13,   //  13
  14,   //  14
  15,   //  15
  16,   //  16
  17,   //  17
  18,   //  18
  19,   //  19
  20,   //  20
  21,   //  21
  22,   //  22
  23,   //  23
  24,   //  24
  25,   //  25
  26,   //  26
  27,   //  27
  28,   //  28
  29,   //  29
  30,   //  30
  31    //  31
  };
  
*/

//fdserial *uart[2];

/*
void i2cMaster()
{
  mbBusM = i2c_newbus(8,  9,   0);
  reg = i2cslave_regAddr(mbBusS);

  char command, pin;
  int arg1, arg2, pinState;
  
  pause(100);
  command = FREQOUT; pin = 4; arg1 = 2000; arg2 = 3000;
  i2c_out(mbBusM, 0x42, ARG2, 1, &arg2, 4);
  i2c_out(mbBusM, 0x42, ARG1, 1, &arg1, 4);
  i2c_out(mbBusM, 0x42, PIN1, 1, &pin, 1);
  i2c_out(mbBusM, 0x42, COMMAND, 1, &command, 1);
  while(command)
  {
    i2c_in(mbBusM, 0x42, COMMAND, 1, &command, 1);
  } 

  while(1)
  {
    command = INPUT; pin = 5;
    i2c_out(mbBusM, 0x42, PIN1, 1, &pin, 1);
    i2c_out(mbBusM, 0x42, COMMAND, 1, &command, 1);
    while(command)
    {
      i2c_in(mbBusM, 0x42, COMMAND, 1, &command, 1);
    }
    i2c_in(mbBusM, 0x42, RETVAL, 1, &pinState, 4);

    command = LOW;
    if(pinState) command = HIGH;
    pin = 27;
    i2c_out(mbBusM, 0x42, PIN1, 1, &pin, 1);
    i2c_out(mbBusM, 0x42, COMMAND, 1, &command, 1);
    while(command)
    {
      i2c_in(mbBusM, 0x42, COMMAND, 1, &command, 1);
    } 

    command = HIGH; pin = 26;
    i2c_out(mbBusM, 0x42, PIN1, 1, &pin, 1);
    i2c_out(mbBusM, 0x42, COMMAND, 1, &command, 1);
    while(command)
    {
      i2c_in(mbBusM, 0x42, COMMAND, 1, &command, 1);
    } 
    
    command = PAUSE; arg1 = 100;
    i2c_out(mbBusM, 0x42, ARG1, 1, &arg1, 4);
    i2c_out(mbBusM, 0x42, COMMAND, 1, &command, 1);
    while(command)
    {
      i2c_in(mbBusM, 0x42, COMMAND, 1, &command, 1);
    } 

    command = LOW; pin = 26;
    i2c_out(mbBusM, 0x42, PIN1, 1, &pin, 1);
    i2c_out(mbBusM, 0x42, COMMAND, 1, &command, 1);
    while(command)
    {
      i2c_in(mbBusM, 0x42, COMMAND, 1, &command, 1);
    } 
    
    command = PAUSE; arg1 = 100;
    i2c_out(mbBusM, 0x42, ARG1, 1, &arg1, 4);
    i2c_out(mbBusM, 0x42, COMMAND, 1, &command, 1);
    while(command)
    {
      i2c_in(mbBusM, 0x42, COMMAND, 1, &command, 1);
    }
  }
}  

*/ 

int main()
{  
  //cog_run(i2cMaster, 512);
  //mbBusS = i2cslave_start(27, 26, 0x5D);

  mbBusS = i2cslave_start(28, 29, 0x5D);  // set to the Propller's EEPROM i2c bus
  reg = i2cslave_regAddr(mbBusS);
  int i = 0;
  sirc_setTimeout(70);
  
  high(20); // Turn on one of the on-board LEDs - for testing pusposes currently.
  high(23); // Assert to connect the i2c bus between Propeller and Micro:bit together.
  
  while(1)
  {
    int command = 0;
    while(!command)
    {
      command = i2cslave_getReg(mbBusS, COMMAND);
    }
    int pin1 = (int) reg[PIN1];
    int pin2 = (int) reg[PIN2];
    unsigned int state = (unsigned int) reg[STATE];
    int arg1, arg2, arg3, arg4, arg5;
    int retVal = 0;
    //char retStr[512];

    memcpy(&arg1, &reg[ARG1], 4);
    memcpy(&arg2, &reg[ARG2], 4);
    memcpy(&arg3, &reg[ARG3], 4);
    memcpy(&arg4, &reg[ARG4], 4);
    memcpy(&arg5, &reg[ARG5], 4);
    //memcpy(&retStr, &reg[STRBUF], 512);
    
    switch(command)
    {
      case HIGH:
        high(pin1);
        break;
      case LOW:
        low(pin1);
        break;
      case TOGGLE:
        set_direction(pin1, 1);
        toggle(pin1);
        break;
      case INPUT:
        retVal = input(pin1);
        memcpy(&reg[RETVAL], &retVal, 4);
        break;
      case GETDIRS:
        retVal = get_directions(pin1, pin2);
        memcpy(&reg[RETVAL], &retVal, 4);
        break;
      case SETDIRS:
        set_directions(pin1, pin2, state);
        break;
      case GETSTATES:
        retVal = get_states(pin1, pin2);
        memcpy(&reg[RETVAL], &retVal, 4);
        break;
      case SETSTATES:
        set_outputs(pin1, pin2, state);
        break;
      case PAUSE:
        pause(arg1);
        break;
      case FREQOUT:
        freqout(pin1, arg1, arg2);
        break;
      case PULSOUT:
        pulse_out(pin1, arg1);
        break;
      case PULSIN:
        retVal = pulse_in(pin1, state);
        memcpy(&reg[RETVAL], &retVal, 4);
        break;
      case COUNT:
        retVal = pulse_in(pin1, arg1);
        memcpy(&reg[RETVAL], &retVal, 4);
        break;
      case RCTIME:
        retVal = rc_time(pin1, state);
        memcpy(&reg[RETVAL], &retVal, 4);
        break;
      case SERVO_ANGLE:
        servo_angle(pin1, arg1);
        break;
      case SERVO_SPEED:
        servo_speed(pin1, arg1);
        break;
      case SERVO_SET:
        servo_set(pin1, arg1);
        break;
      case SERVO_SETRAMP:
        servo_setramp(pin1, arg1);
        break;
      case SERVO_DISABLE:
        servo_disable(pin1);
        break;
      case PING_ECHO:
        retVal = ping(pin1);
        memcpy(&reg[RETVAL], &retVal, 4);
        break;
      case SIRC:
        retVal = sirc_button(pin1);
        memcpy(&reg[RETVAL], &retVal, 4);
        break;
        /*
      case UART_INIT:
        uart[pin1] = fdserial_open(pin2, state, arg2, arg1);  // using pin1 to define which instance is being called, since pins are defined only in the init call.
        break;
      case UART_RX_LEN:
        retVal = fdserial_rxCount(uart[pin1]);
        memcpy(&reg[RETVAL], &retVal, 4);
        break;
      case UART_READ:
        readStr(uart[pin1], retStr, arg1);
        memcpy(&reg[STRBUF], &retStr, arg1);
        break;
      case UART_WRITE:
        for (int l = 0; l < 512; l++) {
          char ch = reg[STRBUF + l];
          if (ch != 0) {
            writeChar(uart[pin1], ch);
          } else {
            writeChar(uart[pin1], 0);
            break;
          }                       
        }
        */


    }
    //print("i:%d, ", i++);
    //for(int n = 0; n < 32; n++) print("%d:%d, ", n, reg[n]);
    //print("\n");
    //pause(100);
    i2cslave_putReg(mbBusS, 0, 0);
  }
}   
  

