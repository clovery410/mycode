#include <stdio.h>

int a[] = {2, 300, 8, 23, 90, 41, 7};

int find_largest(int *a, int n);

int main(void)
{
  int size_t = sizeof(a) / sizeof(a[0]);
  
  printf("The largest value if array is: %d\n", find_largest(a, size_t));

  return 0;
}
int find_largest(int *a, int n)
{
  int max, *p = a;

  max = *p;
  for (p = a + 1; p < a + n; p++) {
    if (*p > max) {
      max = *p;
    }
  }

  return max;
}
