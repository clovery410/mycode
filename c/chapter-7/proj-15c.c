#include <stdio.h>

int main(void)
{
  long i, num, factor;

  printf("Enter a positive integer: ");
  scanf("%ld", &num);

  for (i = 1, factor = 1; i <= num; i++) {
    if ((long) (factor * i) < factor)
      break;
    else 
      factor *= i;
  }

  printf("Factorial of %ld: %ld\n", i - 1, factor);

  return 0;
}
