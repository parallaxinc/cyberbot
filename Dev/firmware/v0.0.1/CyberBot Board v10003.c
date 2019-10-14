/*
  MicroBit Bot Firmware Dev with Reset Monitor v0_4_0.c
  
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
#include "i2crepeat.h"
#include "servo360.h"
#include "abdrive360.h" 
//#include "abcalibrate360.h"

#define reboot() __builtin_propeller_clkset(0x80)

//                       mamipa
#define FIRMWARE_VERSION  10003

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

#define I2C_REPEAT     40

#define AB360_CALIBRATE    60
#define AB360_CONNECT      61
#define AB360_SPEED        62
#define AB360_GOTO         63
#define AB360_SETRAMP      64

/*
#define SERVO360_CONNECT   70
#define SERVO360_ANGLE     71
#define SERVO360_SPEED     72
#define SERVO360_GOTO      73
#define SERVO360_SETRAMP   74
#define SERVO360_GET_ANGLE 75
#define SERVO360_GET_ANGLE_CALC 56
*/

#define COGS_FREE          97
#define REPORT_VERSION     98
#define HANDSHAKE          99

#define PWR_LED_WARN       25
#define PWR_BRN_DET        24
//#define PWR_LED_WARN   15
//#define PWR_BRN_DET   14

#define APP_CTR_POSDET (0b01000 << 26)
#define APP_CTR_NEGDET (0b01100 << 26) | PWR_BRN_DET  

#define APP_CTR_NEGEDG (0b01110 << 26) | PWR_BRN_DET  

// ------ Global Variables and Objects ------
i2c *mbBusM;
i2cslave *mbBusS;
static char *_i2_reg;
volatile int running_flag = 0;

int pwmPin[] = {-1, -1, -1, -1};
//int pinAssign[] = {-1, -1, -1, -1};
//int dutyAssign[] = {-1, -1, -1, -1};
//int chanAssign[] = {0, 1, 2, 3};

int removePwm(int);
int assignPwm(int, int);
void resetMonitor();
void servo_runOnce();

pwm2ch *pwmA;
pwm2ch *pwmB;
dac2ch *dacA;
i2crepeat *i2crep;

volatile int brnState = 0;
volatile int consecutive = 0;
volatile int consecutiveA = 0;
volatile int consecutiveB = 0;
volatile int rm_reps = 0;
volatile int _cogs_free = 8;
volatile int _servo_running = 0;


// ------ Main Program ------
int main() 
{
  _cogs_free--;
  drive_suppress_eeprom(1);

  int microsecond = CLKFREQ / 1000000;
  mbBusS = i2cslave_open(28, 29, 0x5D);
  _cogs_free--;
  _i2_reg = i2cslave_regAddr(mbBusS);

  sirc_setTimeout(70);   // Set Sony IR remote time out to 70 ms

  high(23);   // Connect the Propeller and micro:bit i2c busses together
  
  cog_run(resetMonitor, 128);
  _cogs_free--;
  
  while(1) 
  {
    // Wait for command to become nonzero.  Command is always the last register to
    // be populated, so it means the command is ready.
    int command = 0;
    while(!command) 
    {
      command = i2cslave_getReg(mbBusS, COMMAND);
    }

    // This is just for startup.  After the Propeller detects that the micro:bit
    // has taken control of the I2C bus, the Propeller lets go.
    input(23);  
    
    //     
    int pin1 = _i2_reg[PIN1];
    int pin2 = _i2_reg[PIN2];
    if (pin2 == 33) pin2 = -1;
    _i2_reg[PIN2] = -1;
    unsigned int state = (unsigned int) _i2_reg[STATE];
    _i2_reg[STATE] = 0;
    int arg1, arg2, arg3, arg4, arg5;
    int retVal = 0;
    
    memcpy(&arg1, &_i2_reg[ARG1], 4); memcpy(&_i2_reg[ARG1], &retVal, 4);
    memcpy(&arg2, &_i2_reg[ARG2], 4); memcpy(&_i2_reg[ARG2], &retVal, 4);
    memcpy(&arg3, &_i2_reg[ARG3], 4); memcpy(&_i2_reg[ARG3], &retVal, 4);
    memcpy(&arg4, &_i2_reg[ARG4], 4); memcpy(&_i2_reg[ARG4], &retVal, 4);
    memcpy(&arg5, &_i2_reg[ARG5], 4); memcpy(&_i2_reg[ARG5], &retVal, 4);
    
    if (
             command == SETDIRS 
          || command == SETSTATES 
          || command == QTI_READ
       ) 
    {
      for (int j = pin2; j <= pin1; j++) removePwm(j);
    } 
    else if ( 
              command == IR_DETECT 
              || command == SHIFTIN 
              || command == SHIFTOUT 
              //|| command == AB360_CONNECT 
              //|| command == I2C_REPEAT
            ) 
    {
      removePwm(pin1);
      removePwm(pin2);
    } 
    //else if (command != GETDIRS && command != GETSTATES && command != PAUSE && command != PWM_OUT && command != SERVO_SETRAMP && command != SERVO_DISABLE) 
    else if(    command == HIGH
             || command == LOW
             || command == INPUT
             || command == TOGGLE
             || command == PULSIN
             || command == PULSOUT
             || command == COUNT
             || command == FREQOUT
             || command == RCTIME
             || command == PING_ECHO   
             || command == SIRC
           )
    {
      removePwm(pin1);
    }
    
    if ((command != PAUSE && pin1 > -1 && pin1 < 28 && pin2 < 28) || command == PAUSE) 
    {
      //char temp[] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
      int n = 2;
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
          memcpy(&_i2_reg[RETVAL], &retVal, 4);
          break;
        case GETDIRS:
          retVal = get_directions(pin1, pin2);
          memcpy(&_i2_reg[RETVAL], &retVal, 4);
          break;
        case SETDIRS:
          set_directions(pin1, pin2, state);
          break;
        case GETSTATES:
          retVal = get_states(pin1, pin2);
          memcpy(&_i2_reg[RETVAL], &retVal, 4);
          break;
        case SETSTATES:
          set_outputs(pin1, pin2, state);
          break;

        case AB360_CONNECT:
          drive_suppress_eeprom(1);
          drive_encoderPins(16, 17);
          drive_servoPins(18, 19);
          drive_speed(0,0);
          _cogs_free--;
          break;
        case AB360_GOTO:
          drive_goto(arg1, arg2);
          break;
        case AB360_SPEED:
          drive_speed(arg1, arg2);
          break;
        case AB360_SETRAMP:
          drive_setAcceleration(arg1, arg2);
          break;

        case QTI_READ:
          if (arg1 < 10) 
          {
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
          memcpy(&_i2_reg[RETVAL], &retVal, 4);
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
          memcpy(&_i2_reg[RETVAL], &retVal, 4);
          break;
        case PULSOUT:
          pulse_out(pin1, arg1);
          break;
        case PULSIN:
          retVal = pulse_in(pin1, state);
          memcpy(&_i2_reg[RETVAL], &retVal, 4);
          break;
        // arg1 is ms duration
        case COUNT:
          retVal = count(pin1, arg1);
          memcpy(&_i2_reg[RETVAL], &retVal, 4);
          break;
        case RCTIME:
          if (arg1 < 10) 
          {
            arg1 = 1000;
          }
          if (arg2 < 1 || arg2 > 1023) 
          {
            set_output(pin1, state);
            set_direction(pin1, 1);
            dT = microsecond * arg1;
            waitcnt(dT + CNT);
          } 
          else 
          {
            //assignPwm(pin1, arg2); 
            dac_ctr_res(10);
            dac_ctr(pin1,0,arg2);
            dT = microsecond * arg1;
            waitcnt(dT + CNT);
            dac_ctr_stop();
            //removePwm(pin1);
          }
          retVal = rc_time(pin1, state);
          memcpy(&_i2_reg[RETVAL], &retVal, 4);
          break;
        case PWM_OUT:
          if(arg1 == -1)
          {
            removePwm(pin1); 
          }
          else
          {
            arg1 = constrainInt(arg1, 0, 1023);
            assignPwm(pin1, arg1);
          }            
          break;
        case SERVO_ANGLE:
          if(!_servo_running) servo_runOnce();
          servo_angle(pin1, arg1 * 10);
          break;
        case SERVO_SPEED:
          if(!_servo_running) servo_runOnce();
          if (pin2 >= 0 && pin2 < 33) 
          {
            servo_speed(pin2, arg2);
          }
          servo_speed(pin1, arg1);
          break;
        case SERVO_SET:
          if(!_servo_running) servo_runOnce();
          servo_set(pin1, arg1);
          break;
        case SERVO_SETRAMP:
          if(!_servo_running) servo_runOnce();
          if(servo_get(pin1) < 0)
          {
            servo_speed(pin1, 0);
            //pause(40);
            servo_setramp(pin1, arg1);  
            //pause(40);
            servo_speed(pin1, 0);
            //servo_disable(pin1);
            //pause(40);
          }
          else
          {
            servo_setramp(pin1, arg1);
          }            
          break;
        case SERVO_DISABLE:
          servo_disable(pin1);
          break;

        case PING_ECHO:
          retVal = ping(pin1);
          memcpy(&_i2_reg[RETVAL], &retVal, 4);
          break;
        case SIRC:
          retVal = sirc_button(pin1);
          memcpy(&_i2_reg[RETVAL], &retVal, 4);
          break;
          //
        case I2C_REPEAT:
          if(!i2crep)
          {
            _cogs_free--;
            i2crep = i2crepeat_slave(mbBusS, arg1, arg2);
            //i2crep = i2crepeat_slave(mbBusS, pin1, pin2);
          } 
          //    
        case SHIFTOUT:
          //print("c:%d, p1:%d, p2:%d, s:%d, a1:%d, a2:%d\r", command, pin1, pin2, state, arg1, arg2);
          shift_out(pin1, pin2, state, arg1, arg2);
          break;
        case SHIFTIN:
          //print("c:%d, p1:%d, p2:%d, s:%d, a1:%d\r", command, pin1, pin2, state, arg1);
          retVal = shift_in(pin1, pin2, state, arg1);
          //print("retVal = %d\r", retVal);
          memcpy(&_i2_reg[RETVAL], &retVal, 4);
          break;
        /*  
        case SEROUT:
          memcpy(&temp[0], &arg2, 4); 
          memcpy(&temp[4], &arg3, 4); 
          memcpy(&temp[8], &arg4, 4); 
          memcpy(&temp[12], &arg5, 4); 
          //print("pin1 = %d, arg1 = %d, temp = %2s\r", pin1, arg1, temp);
          high(pin1);
          //simpleterm_close();
          simpleterm_reopen(-1, pin1, 0, arg1);
          int p = 0;
          print("%s", temp);
          // while(temp[p] != 0)
          //{
          //  putChar(temp[p++]);
          //}  
          high(pin1);
          //simpleterm_close();
          //input(pin1);
          break;
        case SERIN:
          simpleterm_close();
          simpleterm_reopen(pin1, pin1, 0, arg1);
          char buf[4] = {0,0,0,0};
          getStr(buf, arg2); 
          memcpy(&_i2_reg[RETVAL], &buf, 4);
          simpleterm_close();
          break;
        */         




        case COGS_FREE:
          retVal = _cogs_free;
          memcpy(&_i2_reg[RETVAL], &retVal, 4);
          break;
        case REPORT_VERSION:
          retVal = FIRMWARE_VERSION;
          memcpy(&_i2_reg[RETVAL], &retVal, 4);
          break;
        case HANDSHAKE:
          input(23);
          pause(15);
          running_flag = 1;
          break;
          
/*
        case AB360_CALIBRATE:
          cal_servoPins(18, 19);
          cal_encoderPins(16, 17);
          high(20);
          high(21);
          cal_activityBot();
          low(20);
          low(21);
          break;
*/ 
        
/*
        case SERVO360_CONNECT:
          servo360_angle(pin1, pin2);
          break;
        case SERVO360_ANGLE:
          servo360_angle(pin1, arg1);
          break;
        case SERVO360_SPEED:
          servo360_speed(pin1, arg1);
          break;
        case SERVO360_GOTO:
          servo360_goto(pin1, arg1);
          break;
        case SERVO360_SETRAMP:
            servo360_setAcceleration(pin1, arg1);
          break;
        case SERVO360_GET_ANGLE:
          servo360_getAngle(pin1);
          memcpy(&_i2_reg[RETVAL], &retVal, 4);
          break;
        case SERVO360_GET_ANGLE_CALC:
          servo360_getAngleCalc(pin1);
          memcpy(&_i2_reg[RETVAL], &retVal, 4);
          break;
*/

      }
      i2cslave_putReg(mbBusS, 0, 0);
    }
  }
}


void resetMonitor() 
{
  //high(21);
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
    //high(21);
    
    if( running_flag && !input(23) ) 
    {
      reboot();
    }
    
    if( (CNT - tp) >= dtp )
    {
      rm_reps++;
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
        if( (rm_reps % brnState) == 0 ) toggle(PWR_LED_WARN);
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
  int instance, channel, n;
  
  if(ppin == 20 || ppin == 21)
  {
    if(!dacA)
    {
      _cogs_free--;
      dacA = dac2ch_start(10);
    }      
  }
      
  if (ppin == 20) 
  {
    dac2ch_set(dacA, 20, 0, val);
  } 
  else if (ppin == 21) 
  {
    dac2ch_set(dacA, 21, 1, val);
  } 
  else 
  {  
    // Check if pin is already in use.
    for(n = 0; n < 4; n++)
    {
      if(pwmPin[n] == ppin) break;
    }
    
    // If pin not in use...
    if(n == 4)
    {
      // Check if there's an available slot and return if no.
      for(n = 0; n < 4; n++)
      {
        if(pwmPin[n] == -1) break;
      }
      
      // If available slot, add pin.  If not, return.
      if(n != 4)
      {
        pwmPin[n] = ppin;
      }
      else
      {
        return n;
      }      
    }    
      
    // Store pin in available slot and use index n to calculate
    // PWM instance and channel
    instance = n / 2;
    channel = n % 2;
      
    // Set PWM on the instance and channel.
    if(!instance)
    {
      if(!pwmA)
      {
        _cogs_free--;
        pwmA = pwm2ch_start(1023);
      }      
      pwm2ch_set(pwmA, ppin, channel, val);
    }      
    else
    {
      if(!pwmB)
      {
        _cogs_free--;
        pwmB = pwm2ch_start(1023);
      }      
      pwm2ch_set(pwmB, ppin, channel, val);
    }
  }          

  return n;
}


int removePwm(int ppin) 
{
  int instance, channel, n;
  
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
    // Check if pin is already in use.
    for(n = 0; n < 4; n++)
    {
      if(pwmPin[n] == ppin) break;
    }
  
    // If pin in use, disable its PWM.
    if(n < 4)
    {
      pwmPin[n] = -1;
      instance = n / 2;
      channel = n % 2;
  
      if(!instance)
      {
        pwm2ch_set(pwmA, ppin, channel, -1);
        if( pwmA && (pwmPin[0] == -1) && (pwmPin[1] == -1) )
        {
          _cogs_free++;
          pwm2ch_stop(pwmA);
          pwmA = 0;
        }      
      }      
      else
      {
        pwm2ch_set(pwmB, ppin, channel, -1);
        if( pwmB && (pwmPin[2] == -1) && (pwmPin[3] == -1) )
        {
          _cogs_free++;
          pwm2ch_stop(pwmB);
          pwmB = 0;
        }      
      }      
    }
  }

  if(dacA)
  {
    if( (dacA->ctra == 0) && (dacA->ctrb == 0) )
    {
      _cogs_free++;
      dac2ch_stop(dacA);
      dacA = 0;
    }
  }    

  return n;
}


void servo_runOnce(void)
{
  _cogs_free--;
  _servo_running = 1;
}  
  
