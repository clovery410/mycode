#include <stdio.h>

double median(double x, double y, double z);

int main(void)
{
  double x, y, z;

  printf("Enter three numbers: ");
  scanf("%lf%lf%lf", &x, &y, &z);

  printf("The median number is %g\n", median(x, y, z));

  return 0;
}

double median(double x, double y, double z)
{
  double middle = x;

  if (x <= y && x <= z) {
    if (y <= z)
      middle = y;
    else
      middle = z;
  }
  else if (x >= y && x >= z) {
    if (y >= z)
      middle = y;
    else
      middle = z;
  }

  return middle;
}
