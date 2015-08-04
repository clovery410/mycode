#include <stdio.h>
#include <stdlib.h>

#define LEN 3

int sum_two_array(const int a[][LEN], int n);

int main(void)
{
  int total;
  int b[][LEN] = {{1, 2, 3},
		  {4, 5, 6},
		  {7, 8, 9},
		  {10, 11, 12},
		  {13, 14, 15}};
  int n = sizeof(b) / sizeof(b[0]);
  total = sum_two_array(b, n);

  printf("Total is: %d\n", total);

  return 0;
}

int sum_two_array(const int a[][LEN], int n)
{
  int *p, sum = 0;

  //int element = *(*(a + n - 1) + LEN - 1);
  //printf("Last element is: %d\n", element);
  //printf("First element is: %d\n", **a);
  for (p = *a; p < *(a + n - 1) + LEN; p++) {
    sum += *p;
  }
  return sum;
}
