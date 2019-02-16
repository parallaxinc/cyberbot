/*
  i2cRepeater.h
*/

typedef volatile struct i2crepeat_s
{
  volatile int crmask, crmaskn, drmask, drmaskn, cmask, cmaskn, dmask, dmaskn;
  volatile int cog;
} i2crepeat_t;

typedef volatile i2crepeat_t i2crepeat;


i2crepeat *i2crepeat_slave(void *i2cbus, int sclRepeated, int sdaRepeated);
i2crepeat *i2crepeat_master(void *i2cbus, int sclRepeated, int sdaRepeated);

void i2crepeat_close();
                 
