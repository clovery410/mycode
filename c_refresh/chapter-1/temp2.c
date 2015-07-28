#include <stdio.h>

int main (void)
{
  int fahr, celsius;
  int lower, upper, step;

  lower = -20;
  upper = 150;
  step = 10;

  for (celsius = lower; celsius <= upper; celsius += step)
    {
      fahr = (9 / 5) * celsius + 32;
      printf("%3d\t%6d\n", celsius, fahr);

    }
  return 0;

}
