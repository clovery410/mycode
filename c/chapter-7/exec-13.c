#include <stdio.h>

int main(void)
{
  char c = '\1';
  short s = 2;
  int i = -3;
  long m = 5;
  float f = 6.5f;
  double d = 7.5;

  printf("%d %ld %f %lf %lf %d\n", c * i, s + m, f / c, d / s, f - d, (int) f);

  return 0;
}
