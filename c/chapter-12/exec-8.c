#include <stdio.h>

#define N 10

void store_zeros(int a[], int n);

int main(void)
{
  int b[N], *q;

  store_zeros(b, N);

  for (q = b; q < b + N; q++) {
    printf("%d ", *q);
  }
  printf("\n");

  return 0;
}

void store_zeros(int a[], int n)
{
  int *p;

  for (p = a; p < a + n; p++)
    *p = 0;
}
