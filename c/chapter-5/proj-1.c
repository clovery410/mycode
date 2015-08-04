#include <stdio.h>

int main(void)
{
  int n, i;

  printf("Enter a number (assume no more than four digits): ");
  scanf("%d", &n);

  if (n / 1000)
    i = 4;
  else if (n / 100)
    i = 3;
  else if (n / 10)
    i = 2;
  else
    i = 1;

  printf("The number %d has %d digits\n", n, i);

  return 0;
}
