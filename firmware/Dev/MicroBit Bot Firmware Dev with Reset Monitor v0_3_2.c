/*
  MicroBit Bot Firmware Dev with Reset Monitor v0_3_1.c
  
  3/7/19
  This is a development version of the 0.3 firmware that uses circuits connected
  to P14 and P15 to emulate circuits on the next board revision that will have 
  similar circuits on P24 and P25.  This version of the firmware works with: 

  cyberbot/library/parallax_min_0_3.py 
  https://github.com/parallaxinc/cyberbot/blob/master/library/parallax_min_0_3.py
  
  Test circuit:

    P15: Active-high red LED
    P14: Active Low brown-out detector prototyped with a potentiometer
         Connect A terminal to 5 V
         Connect B terminal to GND
         Connect W terminal to P14
         Tune Pot so that the voltage at W is 1.7 V.
         
  Battery pack: 
  
    5 alkaline cells - use P16 and P17 for left and right servos
    5 NiMH cells     - use P18 and P19 for left and right servos
    
    NOTE: Make sure to update your bot application code accordingly
    
  Behaviors:
    
    Blinks at 5 Hz if brownout is detected.  
    Blinks at 2.5 Hz if a symptom (I have not been able to reproduce) is 
    detected where the brownout only occurs during servo pulses.  
*/

// ------ Libraries and Definitions ------
#include "simpletools.h"
#include "simplei2c.h"
#include "i2cslave.h"
#include "servo.h"
#include "ping.h"
#include "sirc.h"
#include "pwm2ch.h"
#include "dac2ch.h"


#define reboot() __builtin_propeller_clkset(0x80)

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
#define SERVO_DRIVE    34

#define PING_ECHO      29
#define SIRC           30
#define IR_DETECT      31
#define PWM_OUT        32
#define QTI_READ       33

#define HANDSHAKE      99


#define PWR_LED_WARN   25
#define PWR_BRN_DET    24
//#define PWR_LED_WARN   15
//#define PWR_BRN_DET   14

#define APP_CTR_POSDET (0b01000 << 26)
#define APP_CTR_NEGDET (0b01100 << 26) | PWR_BRN_DET  

#define APP_CTR_NEGEDG (0b01110 << 26) | PWR_BRN_DET  

// ------ Global Variables and Objects ------
i2c *mbBusM;
i2cslave *mbBusS;
static char *reg;
volatile int running_flag = 0;

int pinAssign[] = {-1, -1, -1, -1};
int dutyAssign[] = {-1, -1, -1, -1};
int chanAssign[] = {0, 1, 2, 3};

int removePwm(int);
int assignPwm(int, int);
void resetMonitor();

pwm2ch *pwmA;
pwm2ch *pwmB;
dac2ch *dacA;

volatile int brnState = 0;
volatile int consecutive = 0;
volatile int consecutiveA = 0;
volatile int consecutiveB = 0;
volatile int reps = 0;

// ------ Main Program ------
int main() 
{
  int microsecond = CLKFREQ / 1000000;
  mbBusS = i2cslave_open(28, 29, 0x5D);
  reg = i2cslave_regAddr(mbBusS);

  // Start PWM processes
  pwmA = pwm2ch_start(1023);
  pwmB = pwm2ch_start(1023);
  dacA = dac2ch_start(10);
  
  sirc_setTimeout(70);   // Set Sony IR remote time out to 70 ms

  high(23);   // Connect the Propeller and micro:bit i2c busses together
  
  cog_run(resetMonitor, 128);
  //int brnStatePrev = brnState;
  //print("brnState = %d\r", brnState);
  while(1) {
    //if(brnState != brnStatePrev) print("brnState = %d\r", brnState);
    //brnStatePrev = brnState;
    int command = 0;
    while(!command) {
      command = i2cslave_getReg(mbBusS, COMMAND);
    }
    int pin1 = reg[PIN1];
    int pin2 = reg[PIN2];
    if (pin2 == 33) pin2 = -1;
    reg[PIN2] = -1;
    unsigned int state = (unsigned int) reg[STATE];
    reg[STATE] = 0;
    int arg1, arg2, arg3, arg4, arg5;
    int retVal = 0;
    
    memcpy(&arg1, &reg[ARG1], 4); memcpy(&reg[ARG1], &retVal, 4);
    memcpy(&arg2, &reg[ARG2], 4); memcpy(&reg[ARG2], &retVal, 4);
    memcpy(&arg3, &reg[ARG3], 4); memcpy(&reg[ARG3], &retVal, 4);
    memcpy(&arg4, &reg[ARG4], 4); memcpy(&reg[ARG4], &retVal, 4);
    memcpy(&arg5, &reg[ARG5], 4); memcpy(&reg[ARG5], &retVal, 4);
    
    if (command == SETDIRS || command == SETSTATES || command == QTI_READ) 
    {
      for (int j = pin2; j <= pin1; j++) removePwm(j);
    } 
    else if (command == IR_DETECT) 
    {
      removePwm(pin1);
      removePwm(pin2);
    } 
    else if (command != GETDIRS && command != GETSTATES && command != PAUSE && command != PWM_OUT && command != SERVO_SETRAMP && command != SERVO_DISABLE) 
    {
      removePwm(pin1);
    }
    
    if ((command != PAUSE && pin1 > -1 && pin1 < 28 && pin2 < 28) || command == PAUSE) 
    {
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
          if (arg1 < 10) 
          {
            arg1 = 1000;
          }
          if (arg2 < 1 || arg2 > 1023) 
          {
            set_direction(pin1, 1);
            set_output(pin1, state);
            dT = microsecond * arg1;
            waitcnt(dT + CNT);
          } 
          else 
          {
            assignPwm(pin1, arg2); 
            dT = microsecond * arg1;
            waitcnt(dT + CNT);
            removePwm(pin1);
          }
          retVal = rc_time(pin1, state);
          memcpy(&reg[RETVAL], &retVal, 4);
          break;
        case PWM_OUT:
          // arg1 range 0-1023
          arg1 = constrainInt(arg1, 0, 1023);
          assignPwm(pin1, arg1);
          break;
        case SERVO_ANGLE:
          servo_angle(pin1, arg1);
          break;
        case SERVO_SPEED:
          if (pin2 >= 0 && pin2 < 33) 
          {
            servo_speed(pin2, arg2);
          }
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
        case HANDSHAKE:
          input(23);
          pause(15);
          running_flag = 1;
          break;
      }
      i2cslave_putReg(mbBusS, 0, 0);
    }
  }
}


void resetMonitor() 
{
  pause(100);
  low(PWR_LED_WARN);
  
  
  CTRA = APP_CTR_NEGDET;
  FRQA = 1;
  PHSA = 0;

  CTRB = APP_CTR_NEGEDG;
  FRQB = 1;
  PHSB = 0;

  int tp = CNT;
  int dtp = CLKFREQ/10;
  //int dtBrown = 
  
  while(1) 
  {
    if( running_flag && !input(23) ) 
    {
      reboot();
    }
    
    if( (CNT - tp) >= dtp )
    {
      reps++;
      tp += dtp;

      // More than 50 ms in 3 consecutive 100 ms samples, blink at 5 Hz
      if( (PHSA > (CLKFREQ / 20) ) )
      {
        consecutive = 0;
        consecutiveA++;
        if(consecutiveA > 3)
        {
          brnState = 1;
        }          
      }        
      // > 1 ms every 20 ms, blink at 2.5 Hz
      //
      else if( (PHSA > (CLKFREQ / 1000) ) && (PHSB > 1) && (PHSA < ((CLKFREQ / 1000) * 5) ) )
      {
        consecutive = 0;
        consecutiveB++;
        if(consecutiveB > 3)
        {
          brnState = 2;
        }          
      } 
      // Blink for 10 seconds if no futher brownouts are detected      
      else
      {
        consecutive++;
        if(consecutive > 10)
        {
          consecutiveA = 0;
          consecutiveB = 0;
        } 
        if(consecutive > 50)
        {
          consecutive = 0;
          brnState = 0;
        }                   
      } 
             
      PHSA = 0;
      PHSB = 0;
      
      if(brnState)
      {
        if( (reps % brnState) == 0 ) toggle(PWR_LED_WARN);
      }
      else
      {
        low(PWR_LED_WARN);
      }        
    }      
  }
}


int assignPwm(int ppin, int val) 
{
  int loc = 4;
  if (ppin == 20) {
    dac2ch_set(dacA, 20, 0, val);
  } 
  else if (ppin == 21) 
  {
    dac2ch_set(dacA, 21, 1, val);
  } 
  else 
  {
    loc = -1;
    for (int idx = 0; idx < 4; idx++) 
    {
      if (ppin == pinAssign[idx]) 
      {
        loc = idx;
        break;
      }
    }
    if (loc == -1) {
      for (int idx = 0; idx < 4; idx++) 
      {
        if (pinAssign[idx] == -1) 
        {
          loc = idx;
          break;
        }
      }
    }
    if (loc == -1) 
    {
      loc = 3;
      int tmpChan = chanAssign[0];
      int tmpDuty = dutyAssign[0];
      for (int idx = 0; idx < 3; idx++) 
      {
      	pinAssign[idx] = pinAssign[idx+1];
        chanAssign[idx] = chanAssign[idx+1];
        dutyAssign[idx] = dutyAssign[idx+1];
      }
      chanAssign[3] = tmpChan;
      dutyAssign[3] = tmpDuty;
    }
    pinAssign[loc] = ppin;
    dutyAssign[loc] = val;
    
    // determine Pwm Instance and Channel
    int inst = (chanAssign[loc] & 2) >> 1;
    int chan = chanAssign[loc] & 1;
    
    // assign PWM
    if (loc >= 0) 
    {
      if (inst) 
      {
        pwm2ch_set(pwmA, ppin, chan, val);
      } else {
        pwm2ch_set(pwmB, ppin, chan, val);
      }
    }
  }
  return loc;
}


int removePwm(int ppin) 
{
  int loc = 4;
  if (ppin == 20) 
  {
    dac2ch_set(dacA, 20, 0, -1);
  } 
  else if (ppin == 21) 
  {
    dac2ch_set(dacA, 21, 1, -1);
  } 
  else 
  {
    loc = -1;
    for (int idx = 0; idx < 4; idx++) 
    {
      if (pinAssign[idx] == ppin) 
      {
        pinAssign[idx] = -1;
        loc = idx;
        break;
      }
    }
    int k = loc;
    if (loc >= 0) 
    {
      int tmpPwm = chanAssign[loc];
      while (k < 3) 
      {
        chanAssign[k] = chanAssign[k + 1];
        pinAssign[k] = pinAssign[k + 1];
        k++;
      }
      chanAssign[3] = tmpPwm;
      pinAssign[3] = -1;
    
      // determine Pwm Instance and Channel
      int inst = (chanAssign[loc] & 2) >> 1;
      int chan = chanAssign[loc] & 1;
    
    	// Turn off PWM
      if (inst) 
      {
        pwm2ch_set(pwmA, ppin, chan, -1);
      } 
      else 
      {
        pwm2ch_set(pwmB, ppin, chan, -1);
      }
  	}
  }
  return loc;
}
