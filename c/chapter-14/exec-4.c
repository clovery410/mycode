#include <stdio.h>

#define AVG(x, y) (((x) + (y)) / 2)
#define AREA(x, y) ((x) * (y))

int main(void)
{
  printf("Problem of avg is: %f\n", 2.0/AVG(1, 3));
  printf("Problem of area is: %f\n", 1.0/AREA(2, 2));

  return 0;
}
