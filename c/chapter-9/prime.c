/* Tests whether a number is prime */

#include <stdio.h>
#include <stdbool.h>

bool is_prime(int n)
{
  int i;

  if (n <= 1)
    return false;
  for (i = 2; i * i <= n; i++)
    if (n % 2 == 0)
      return false;
  return true;
}

int main(void)
{
  int num;

  printf("Enter a number: ");
  scanf("%d", &num);

  if (is_prime(num))
    printf("Prime\n");
  else
    printf("Not prime\n");

  return 0;
}
