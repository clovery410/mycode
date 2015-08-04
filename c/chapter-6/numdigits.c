/* Calculates the number of digits in an integer */

#include <stdio.h>

int main(void)
{
  int n, d = 0;
  
  printf("Enter a nonnegative integer: ");
  scanf("%d", &n);

  do {
    n /= 10;
    d++;
  } while (n > 0);

  printf("The number has %d digit(s).\n", d);

  return 0;
}
