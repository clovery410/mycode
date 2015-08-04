#include <stdio.h>

int main(void)
{
  long long i, num, factor;

  printf("Enter a positive integer: ");
  scanf("%lld", &num);

  for (i = 1, factor = 1; i <= num; i++) {
    if ((long long) (factor * i) < factor)
      break;
    else
      factor *= i;
  }

  printf("Factorial of %lld: %lld\n", i - 1, factor);

  return 0;
}
