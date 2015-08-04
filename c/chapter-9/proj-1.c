#include <stdio.h>

#define LEN 10

void selection_sort(int a[], int n);

int main(void)
{
  int i, a[LEN];

  printf("Enter %d numbers to be sorted: ", LEN);
  for (i = 0; i < LEN; i++)
    scanf("%d", &a[i]);
  
  selection_sort(a, LEN);

  for (i = 0; i < LEN; i++)
    printf("%d ", a[i]);

  printf("\n");
  return 0;
}

void selection_sort(int a[], int n)
{
  int i, index, max = a[0];
  
  if (n == 1) return;

  for (i = 1; i < n; i++)
    if (a[i] > max) {
      max = a[i];
      index = i;
    }
  a[index] = a[n - 1];
  a[n - 1] = max;

  selection_sort(a, n - 1);
}
