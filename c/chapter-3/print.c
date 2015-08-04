#include <stdio.h>

int main(void)
{
  int i, j, a, b;
  float x, y;

  i = 10;
  j = 20;
  x = 43.2892f;
  y = 5527.0f;

  printf("i = %d, j = %d, x = %f, y = %f\n", i, j, x, y);
  scanf("  %d/%d", &a, &b);
  printf("%d, %d\n", a, b);
  return 0;
}
