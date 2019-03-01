#include "simpletools.h"
#include "i2crepeat.h"
#include "i2cslave.h"

i2crepeat *i2crepeat_slave(void *i2cbus, int sclRepeated, int sdaRepeated)
{
  i2cslave *device = (i2cslave *)i2cbus;
  //print("device = %d\r", device);

  i2crepeat_t *i2cRep = (i2crepeat_t *) malloc(sizeof(i2crepeat_t));

  i2cRep->crmask = 1 << sclRepeated;
  i2cRep->crmaskn = ~(i2cRep->crmask);

  //print("crmask  = %32b\r", i2cRep->crmask);
  //print("crmaskn = %32b\r", i2cRep->crmaskn);

  i2cRep->drmask = 1 << sdaRepeated; 
  i2cRep->drmaskn = ~(i2cRep->drmask); 

  //print("drmask  = %32b\r", i2cRep->drmask);
  //print("drmaskn = %32b\r", i2cRep->drmaskn);

  //i2cRep->cmask = device->scl_mask;
  //i2cRep->cmaskn = device->scl_mask_inv;
  i2cRep->cmask = 1 << device->pinSCL;
  i2cRep->cmaskn = ~i2cRep->cmask;
  
  //print("cmask  = %32b\r", i2cRep->cmask);
  //print("cmaskn = %32b\r", i2cRep->cmaskn);

  i2cRep->dmask = 1 << device->pinSDA; 
  i2cRep->dmaskn = ~i2cRep->dmask; 

  //print("dmask  = %32b\r", i2cRep->dmask);
  //print("dmaskn = %32b\r", i2cRep->dmaskn);
  
  //print("%032b\r%032b\r%032b\r%032b\r", 
  //i2cRep->crmask, i2cRep->drmask, i2cRep->cmask, i2cRep->dmask);

  extern unsigned int *i2crepeat_cogc;
  i2cRep->cog = cognew(i2crepeat_cogc, i2cRep) + 1;
  
  //pause(100);
  
  return i2cRep;
}

