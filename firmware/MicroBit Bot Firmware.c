/* SERIAL_TERMINAL USED */

/*
  cyber:bot Firmware
  Propeller firmware mockup as I2C slave I/O expander.
*/

// ------ Libraries and Definitions ------
#include "simpletools.h"
#include "simplei2c.h"
#include "i2cslave.h"
#include "servo.h"
#include "ping.h"
#include "sirc.h"

#define COMMAND        0
#define PIN1           1
#define PIN2           2
#define STATE          3
#define ARG1           4
#define ARG2           8
#define ARG3           12
#define ARG4           16
#define ARG5           20
#define RETVAL         24
#define STRBUF         28

#define HIGH           1
#define LOW            2
#define INPUT          3
#define TOGGLE         4
#define SETDIRS        5
#define GETDIRS        6
#define SETSTATES      7
#define GETSTATES      8

#define PAUSE          9
#define PULSIN         10
#define PULSOUT        11
#define COUNT          12
#define FREQOUT        13
#define RCTIME         16

#define SHIFTIN        17
#define SHIFTOUT       18
#define SEROUT         19
#define SERIN          20

#define SERVO_ANGLE    24
#define SERVO_SPEED    25
#define SERVO_SET      26
#define SERVO_SETRAMP  27
#define SERVO_DISABLE  28

#define PING_ECHO      29
#define SIRC           30
#define IR_DETECT      31
#define PWM_OUT        32
#define QTI_READ       33


// ------ Global Variables and Objects ------
i2c *mbBusM;
i2cslave *mbBusS;
static char *reg;

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

// ------ Main Program ------
int main() {
  int microsecond = CLKFREQ / 1000000;
  mbBusS = i2cslave_open(28, 29, 0x5D);
  reg = i2cslave_regAddr(mbBusS);

  sirc_setTimeout(70);   // Set Sony IR remote time out to 70 ms

  high(23);   // Connect the Propeller and micro:bit i2c busses together
  
  while(1) {
    int command = 0;
    while(!command) {
      command = i2cslave_getReg(mbBusS, COMMAND);
    }
    int pin1 = pinMap[(int) reg[PIN1]];
    int pin2 = pinMap[(int) reg[PIN2]];
    reg[PIN2] = 0;
    unsigned int state = (unsigned int) reg[STATE];
    reg[STATE] = 0;
    int arg1, arg2, arg3, arg4, arg5;
    int retVal = 0;
    
    memcpy(&arg1, &reg[ARG1], 4); memcpy(&reg[ARG1], &retVal, 4);
    memcpy(&arg2, &reg[ARG2], 4); memcpy(&reg[ARG2], &retVal, 4);
    memcpy(&arg3, &reg[ARG3], 4); memcpy(&reg[ARG3], &retVal, 4);
    memcpy(&arg4, &reg[ARG4], 4); memcpy(&reg[ARG4], &retVal, 4);
    memcpy(&arg5, &reg[ARG5], 4); memcpy(&reg[ARG5], &retVal, 4);
    
    switch(command) {
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
      case QTI_READ:
        if (arg1 < 10) {
          arg1 = 230;
        }
        int m = 1 << (pin1 - pin2 + 1);
        m--;
        set_outputs(pin1, pin2, m);
        set_directions(pin1, pin2, m);
        waitcnt(microsecond * 250 + CNT);
        set_directions(pin1, pin2, 0);
        int dT = microsecond * arg1;
        dT = dT < 150 ? 150 : dT;
        waitcnt(dT + CNT);
        retVal = get_states(pin1, pin2);
        memcpy(&reg[RETVAL], &retVal, 4);
        break;
      case PAUSE:
        pause(arg1);
        break;
      case FREQOUT:
        freqout(pin1, arg1, arg2);
        break;
      case IR_DETECT:
        freqout(pin2, 1, arg1);
        retVal = input(pin1);
        memcpy(&reg[RETVAL], &retVal, 4);
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
        if (arg1 < 10) {
          arg1 = 1000;
        }
        set_direction(pin1, 1);
        if (arg2 < 1 || arg2 > 1023) {
          set_output(pin1, state);
        } else {
          // PWM the pin... (channel on pin2)
        }
        dT = microsecond * arg1;
        waitcnt(dT + CNT);
        retVal = rc_time(pin1, state);
        memcpy(&reg[RETVAL], &retVal, 4);
        break;
      case PWM_OUT:
        // arg1 range 0-1023
        if (pin1 == 20) {
          // DA for pin 20
        } else if (pin1 = 21) {
          // DA for pin 21
        } else {
          // PWM the pin (channel on pin2)
        }
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
    }
    i2cslave_putReg(mbBusS, 0, 0);
  }
}
