#include <stdio.h>

int main(void)
{
  float n, max;

  for (max = 0.0f;;) {
    printf("Enter a number: ");
    scanf("%f", &n);

    if (n > max)
      max = n;
    
    if (n <= 0)
      break;
  }

  printf("The largest number entered was %.2f\n", max);

  return 0;
}
