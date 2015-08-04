#include <stdio.h>

#define CUBE(x) ((x) * (x) * (x))
#define REMAINDER(n) ((n) % 4)
#define IS_LESS(x, y) ((x) * (y) < 100)

int main(void)
{
  int i = 1, j = 3;
  int n = 15;
  
  printf("The cube value of %d is %d\n", i + j, CUBE(i + j));
  printf("The remainder when %d is divided by 4 is %d\n", n, REMAINDER(n));

  if (IS_LESS(i, j))
    printf("The product of %d and %d is less than 100\n", i, j);
  else
    printf("The product of %d and %d is equal or greater than 100\n", i, j);

  return 0;
}
