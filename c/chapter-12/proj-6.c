#include <stdio.h>

#define N 10

void quicksort(int a[], int *low, int *high);
int *split(int a[], int *low, int *high);

int main(void)
{
  int a[N], *p;

  printf("Enter %d numbers to be sorted: ", N);
  for (p = a; p < a + N; p++) {
    scanf("%d", p);
  }

  quicksort(a, &a[0], &a[N-1]);

  printf("In sorted order: ");
  for (p = a; p < a + N; p++) {
    printf("%d ", *p);
  }
  printf("\n");

  return 0;
}

void quicksort(int a[], int *low, int *high)
{
  int *middle;

  if (low >= high) return;
  middle = split(a, low, high);
  quicksort(a, low, middle - 1);
  quicksort(a, middle + 1, high);
}

int *split(int a[], int *low, int *high)
{
  int part_element = *low;

  for (;;) {
    while (low < high && part_element <= *high) {
      high--;
    }
    if (low >= high) break;
    *low++ = *high;

    while (low < high && part_element >= *low) {
      low++;
    }
    if (low >= high) break;
    *high-- = *low;
  }

  *low = part_element;
  return low;
}
  
