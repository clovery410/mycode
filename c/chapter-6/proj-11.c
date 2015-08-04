#include <stdio.h>

int main(void)
{
  int n, i, j, sum;
  float e;

  printf("Enter the number: ");
  scanf("%d", &n);

  for (i = 1, e = 1.00f; i <= n; i++) {
    for (j = 1, sum = 1; j <= i; j++) 
      sum *= j;
    e += 1.00f / sum;
  }

  printf("The value of e is: %f\n", e);

  return 0;
}
