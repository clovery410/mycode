#include <stdio.h>

#define CHECK(x, y, n) (((x) >= 0 && (x) <= (n-1) && (y) >= 0 && (y) <= (n-1)) ? 1 : 0)
#define MEDIAN(x, y, n) ((x) > (y) ? ((y) > (n) ? (y) : ((x) < (n) ? (x) : (n))) : ((y) < (n) ? (y) : ((n) < (x) ? (x) : (n))))
#define POLYNOMIAL(x) (3 * (x) * (x) * (x) * (x) * (x) + 2 * (x) * (x) * (x) * (x) - 5 * (x) * (x) * (x) - (x) * (x) + 7 * (x) - 6)

int main(void)
{
  int x, y, n;
  x = 2;
  y = 6;
  n = 21;

  printf("%d\n", CHECK(x, y, n));
  printf("%d\n", MEDIAN(x, y, n));
  printf("%d\n", POLYNOMIAL(x));

  return 0;
}
