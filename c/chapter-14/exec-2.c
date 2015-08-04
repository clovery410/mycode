#include <stdio.h>

#define NELEMS(a) ((int) (sizeof(a) / sizeof(a[0])))

int main(void)
{
  int a[] = {1, 2, 3, 4, 5, 6, 7};

  printf("number of elements in array a is: %d\n", NELEMS(a));

  return 0;
}
