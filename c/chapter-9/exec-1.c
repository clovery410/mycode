#include <stdio.h>

double triangle_area(double base, double height);

int main(void)
{
  double base, height, area;

  printf("Enter the base and height: ");
  scanf("%lf %lf", &base, &height);

  area = triangle_area(base, height);

  printf("Triangle area is: %g\n", area);

  return 0;
}

double triangle_area(double base, double height)
{
  double product;
  
  product = base * height;
  return product / 2;
}
