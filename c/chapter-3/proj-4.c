#include <stdio.h>

int main(void)
{
  int first, middle, last;

  printf("Enter phone number [(xxx) xxx-xxxx]: ");
  scanf("(%d) %d-%d", &first, &middle, &last);

  printf("You entered %.3d.%.3d.%.4d\n", first, middle, last);

  return 0;
}
