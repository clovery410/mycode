#include <stdio.h>

/* print Fahrenheit-Celsius table                                                                     
   for fahr = 0, 20, ..., 300 */
main()
{
  float fahr, celsius;
  float lower, upper, step;

  lower = 0;    /* lower limit of temperature scale */
  upper = 300;  /* upper limit */
  step = 20;    /* step size */

  for (fahr = upper; fahr >= lower; fahr = fahr - step) {
    celsius=(5.0/9.0)*(fahr-32.0);
    printf("%3.0f\t%6.0f\n", celsius, fahr);
  }
}
