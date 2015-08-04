#include <stdio.h>
#include <math.h>

int main(void)
{
  int i, num;
  double factor;

  printf("Enter a positive integer: ");
  scanf("%d", &num);

  for (i = 1, factor = 1; i <= num; i++) {
    if (isinf(factor * i))
      break;
    else
      factor *= i;
  }

  printf("Factorial of %d: %lf\n", i - 1, factor);

  return 0;
}
