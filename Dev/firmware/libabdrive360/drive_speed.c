/*
  @file drive_speed.c

  @author Parallax Inc

  @copyright
  Copyright (C) Parallax Inc. 2017. All Rights MIT Licensed.  See end of file.
 
  @brief 
*/
//                                            //                                //  


#include "abdrive360.h"


void drive_speed(int left, int right)
{
  if(!abd360_initialized) drive_init();
  
  servo360_setAcceleration(abd360_pinCtrlLeft, abd360_rampStep * 50);
  servo360_setAcceleration(abd360_pinCtrlRight, abd360_rampStep * 50);
  servo360_setMaxSpeed(abd360_pinCtrlLeft, abd360_speedLimit);
  servo360_setMaxSpeed(abd360_pinCtrlRight, abd360_speedLimit);

  servo360_speed(abd360_pinCtrlLeft, left);
  servo360_speed(abd360_pinCtrlRight, -right);
  //pause(1);
  //waitcnt(CLKFREQ/1000 + CNT);
}   


/**
 * TERMS OF USE: MIT License
 *
 * Permission is hereby granted, free of charge, to any person obtaining a
 * copy of this software and associated documentation files (the "Software"),
 * to deal in the Software without restriction, including without limitation
 * the rights to use, copy, modify, merge, publish, distribute, sublicense,
 * and/or sell copies of the Software, and to permit persons to whom the
 * Software is furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
 * THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
 * FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
 * DEALINGS IN THE SOFTWARE.
 */
