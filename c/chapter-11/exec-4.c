#include <stdio.h>

void swap(int *p, int *q);

int main(void)
{
  int i = 3, j = 5;

  swap(&i, &j);

  printf("Value of i is: %d\n", i);
  printf("Value of j is: %d\n", j);

  return 0;
}

void swap(int *p, int *q)
{
  int temp;

  temp = *p;
  *p = *q;
  *q = temp;
}
