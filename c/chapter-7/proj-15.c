#include <stdio.h>

int main(void)
{
  int i, num; 
  short factor;

  printf("Enter a positive integer: ");
  scanf("%d", &num);

  for (i = 1, factor = 1; i <= num; i++) {
    if ((short) (factor * i) < factor)
      break;
    else
      factor *= i;
  }
  printf("Factorial of %d: %hd\n", i - 1, factor);

  return 0;
}
