#include <stdio.h>

void reduce(int numerator, int denominator, int *reduced_numerator, int *reduced_denominator);

int main(void)
{
  int numer, denom, reduced_n, reduced_d;

  printf("Enter a fraction: ");
  scanf("%d/%d", &numer, &denom);

  reduce(numer, denom, &reduced_n, &reduced_d);

  printf("In lowest terms: %d/%d\n", reduced_n, reduced_d);

  return 0;
}

void reduce(int numerator, int denominator, int *reduced_numerator, int *reduced_denominator)
{
  int remainder;

  *reduced_numerator = numerator;
  *reduced_denominator = denominator;

  while (numerator != 0) {
    remainder = denominator % numerator;
    denominator = numerator;
    numerator = remainder;
  }

  *reduced_numerator /= denominator;
  *reduced_denominator /= denominator;
}
