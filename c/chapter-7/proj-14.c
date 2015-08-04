#include <stdio.h>
#include <math.h>

int main(void)
{
  double num, new_y, old_y = 1.0;

  printf("Enter a positive number: ");
  scanf("%lf", &num);
  
  new_y = (old_y + num / old_y) / 2;
  
  while (fabs(old_y - new_y) >= (new_y * .00001)) {
    old_y = new_y;
    new_y = (old_y + num / old_y) / 2;
  }

  printf("Square root: %lf\n", new_y);

  return 0 ;
}
