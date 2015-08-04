#include <stdio.h>

#define N 10

void max_min(int a[], int n, int *max, int *min);

int main(void)
{
  int i, b[N], big, small;
 
  printf("Enter %d numbers: ", N);

  for (i = 0; i < N; i++) {
    scanf("%d", &b[i]);
  }

  max_min(b, N, &big, &small);

  printf("Largest number is: %d\n", big);
  printf("Smallest number is: %d\n", small);
  
  return 0;
}

void max_min(int a[], int n, int *max, int *min)
{
  int i;

  *max = a[0];
  *min = a[0];
  for (i = 1; i < n; i++) {
    if (a[i] > *max) {
      *max = a[i];
    }
    if (a[i] < *min) {
      *min = a[i];
    }
  }
}
		     
