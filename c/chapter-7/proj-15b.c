#include <stdio.h>

int main(void)
{
  int i, num, factor;

  printf("Enter a positive integer: ");
  scanf("%d", &num);

  for (i = 1, factor = 1; i <= num; i++) {
    if ((int) (factor * i) < factor)
      break;
    else 
      factor *= i;
  }

  printf("Factorial of %d: %d\n", i - 1, factor);

  return 0;
}
