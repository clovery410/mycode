#include <stdio.h>

#define N 10

int *find_largest(int a[], int n);

int main(void)
{
  int b[N], i, *position;

  printf("Enter %d numbers: ", N);
  for (i = 0; i < N; i++) {
    scanf("%d", &b[i]);
  }

  position = find_largest(b, N);
  printf("Largest number is %d\n", *position);

  return 0;
}

int *find_largest(int a[], int n)
{
  int i, *max;

  max = &a[0];
  for (i = 1; i < n; i++) {
    if (a[i] > *max) {
      max = &a[i];
    }
  }

  return max;
}
