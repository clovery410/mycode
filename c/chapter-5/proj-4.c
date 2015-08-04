#include <stdio.h>

int main(void)
{
  float speed;

  printf("Enter a wind speed (in knots): ");
  scanf("%f", &speed);

  if (speed < 1.00f)
    printf("Calm");
  else if (speed <= 3.00f)
    printf("Light air");
  else if (speed <= 27.00f)
    printf("Breeze");
  else if (speed <= 47)
    printf("Gale");
  else if (speed <= 63)
    printf("Storm");
  else
    printf("Hurricane");

  printf("\n");
  return 0;
}
