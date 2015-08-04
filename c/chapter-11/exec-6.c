#include <stdio.h>
#include <stdlib.h>

#define N 10

void find_two_largest(int a[], int n, int *largest, int *second_largest);

int main(void)
{
  int b[N], i, first, second;

  printf("Enter %d numbers: ", N);
  for (i = 0; i < N; i++) {
    scanf("%d", &b[i]);
  }

  find_two_largest(b, N, &first, &second);

  printf("The largest number is: %d\n", first);
  printf("The second largest number is: %d\n", second);

  return 0;
}

void find_two_largest(int a[], int n, int *largest, int *second_largest)
{
  int i = 1, j;

  while (a[i] == a[0] && i < n) {
      i++;
  }  

  if (i == n) {
    printf("All the numbers are the same\n");
    exit(EXIT_SUCCESS);
  }
  else if (a[0] > a[i]) {
    *largest = a[0];
    *second_largest = a[i];
  }
  else {
    *largest = a[i];
    *second_largest = a[0];
  }
  
  for (j = i + 1; j < n; j++) {
    if (a[j] > *largest) {
      *second_largest = *largest;
      *largest = a[j];
    }
    else if (a[j] > *second_largest) {
      *second_largest = a[j];
    }
  }
}
