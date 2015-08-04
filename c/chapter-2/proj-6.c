#include <stdio.h>

int main(void)
{
  int x, y;

  printf("Enter the value of x: ");
  scanf("%d", &x);

  y = ((((3 * x + 2) * x - 5) * x - 1) * x + 7) * x - 6;

  printf("Y is: %d\n", y);

  return 0;
}
