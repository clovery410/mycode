#include <stdio.h>

#define N 10

void max_min(int a[], int n, int *max, int *min);

int main(void)
{
  int a[N], max, min, *p;

  printf("Enter %d numbers: ", N);
  for (p = a; p < a + N; p++) {
    scanf("%d", p);
  }

  max_min(a, N, &max, &min);

  printf("Largest: %d\n", max);
  printf("Smallest: %d\n", min);

  return 0;
}

void max_min(int a[], int n, int *max, int *min)
{
  int *q;

  *max = *min = *a;

  for (q = a; q < a + n; q++) {
    if (*q > *max) {
      *max = *q;
    }
    else if (*q < *min) {
      *min = *q;
    }
  }
}

  
