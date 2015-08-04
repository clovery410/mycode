#include <stdio.h>

int new_power(int x, int n);

int main(void) 
{
  int x, n;

  printf("Enter the base: ");
  scanf("%d", &x);
  printf("Enter the exponent: ");
  scanf("%d", &n);

  printf("The value is: %d\n", new_power(x, n));

  return 0;
}

int new_power(int x, int n)
{
  if (n == 0)
    return 1;
  else if (n % 2 == 0)
    return new_power(x, n / 2) * new_power(x, n / 2);
  else
    return x * new_power(x, n - 1);
}
