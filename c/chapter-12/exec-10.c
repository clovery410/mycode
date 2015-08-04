#include <stdio.h>

int arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

int *find_middle(int *a, int n);

int main(void)
{
  int *p;
  int size_t = sizeof(arr) / sizeof(arr[0]);

  p = find_middle(arr, size_t);
  printf("Middle value is %d\n", *p);

  return 0;
}

int *find_middle(int *a, int n)
{
  return a + n / 2;
}
