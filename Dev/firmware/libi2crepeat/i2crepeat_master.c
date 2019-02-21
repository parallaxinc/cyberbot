#include "simpletools.h"
//#include "simplei2c.h"
#include "i2crepeat.h"

i2crepeat *i2crepeat_master(void *i2cbus, int sclRepeated, int sdaRepeated)
{
  i2c *device = (i2c *)i2cbus;
  //print("device = %d\r", device);

  i2crepeat *i2cRep = (i2crepeat_t *) malloc(sizeof(i2crepeat_t));

  i2cRep->crmask = 1 << sclRepeated;
  i2cRep->crmaskn = ~(i2cRep->crmask);

  //print("crmask  = %32b\r", i2cRep->crmask);
  //print("crmaskn = %32b\r", i2cRep->crmaskn);

  i2cRep->drmask = 1 << sdaRepeated; 
  i2cRep->drmaskn = ~(i2cRep->drmask); 

  //print("drmask  = %32b\r", i2cRep->drmask);
  //print("drmaskn = %32b\r", i2cRep->drmaskn);

  i2cRep->cmask = device->scl_mask;
  i2cRep->cmaskn = device->scl_mask_inv;
  
  //print("cmask  = %32b\r", i2cRep->cmask);
  //print("cmaskn = %32b\r", i2cRep->cmaskn);

  i2cRep->dmask = device->sda_mask; 
  i2cRep->dmaskn = device->sda_mask_inv; 

  //print("dmask  = %32b\r", i2cRep->dmask);
  //print("dmaskn = %32b\r", i2cRep->dmaskn);
  
  //print("%0b\r%0b\r%0b\r%0b\r", i2cRep->crmask, i2cRep->drmask,
  //i2cRep->cmask, i2cRep->dmask);

  extern unsigned int *i2crepeat_cogc;
  i2cRep->cog = cognew(i2crepeat_cogc, i2cRep) + 1;
  
  //pause(100);
  
  return i2cRep;
}


