#include <stdio.h>

int digit(int n, int k);

int main(void)
{
  int n, k;

  printf("Enter number n and number k: ");
  scanf("%d%d", &n, &k);

  printf("The %dth digit (from the right) in %d is: %d\n", k, n, digit(n, k));

  return 0;
}

int digit(int n, int k)
{
  int i = 0;

  for (i = 1; i < k; i++)
    n = n / 10;

  return (n % 10);
}
