#include <stdio.h>

int main(void)
{
  int i, j, sum;
  float e, term;

  printf("Enter the term (a small floating-point number): ");
  scanf("%f", &term);

  for (i = 1, e = 1.00f; ; i++) {
    for (j = 1, sum = 1; j <= i; j++)
      sum *= j;
    if (1.00f / sum < term)
      break;
    e += 1.00f / sum;
  }

  printf("The value of e is: %f\n", e);
  return 0;
}
