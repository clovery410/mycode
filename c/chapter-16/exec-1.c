#include <stdio.h>

struct {
  int x, y;
} x = {1, 2};

struct {
  int x, y;
} y = {3, 4};

int main(void)
{
  printf("%d %d\n", x.x, x.y);
  printf("%d %d\n", y.x, y.y);
  
  return 0;
}
