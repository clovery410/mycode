#include <stdio.h>

int main(void)
{
  int numer, denom, n, d, remainder;

  printf("Enter a fraction: ");
  scanf("%d/%d", &numer, &denom);

  n = numer, d = denom;
  while (n != 0) {
    remainder = d % n;
    d = n;
    n = remainder;
  }
  
  printf("In lowest terms: %d/%d\n", numer / d, denom / d);

  return 0;
}

  
