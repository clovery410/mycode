#include <stdio.h>

#define DOUBLE(x) (2 * (x))

int main(void)
{
  printf("Value of question a is: %d\n", DOUBLE(1+2));
  printf("Value of question b is: %d\n", 4/DOUBLE(2));

  return 0;
}
