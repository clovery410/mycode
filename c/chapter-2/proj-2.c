#include <stdio.h>

int main(void)
{
  int radius;
  float pi = 3.14, volume;
  
  //  volume = 4.0f / 3.0f * pi * radius * radius * radius;

  printf("Please enter the radius of the sphere: ");
  scanf("%d", &radius);

  volume = 4.0f / 3.0f * pi * radius * radius * radius;

  printf("The volume of this sphere is: %.2f\n", volume);

  return 0;
}
