#include <stdio.h>

int main(void)
{
  int i, digit;
  long n;
  int digit_occur[10] = {0};

  printf("Enter a number: ");
  scanf("%ld", &n);

  while (n > 0) {
    digit = n % 10;
    digit_occur[digit] += 1;
    n /= 10;
  }

  printf("Digit:       ");
  for (i = 0; i < 10; i++)
    printf(" %d", i);

  printf("\nOccurrences: ");
  for (i = 0; i < 10; i++)
    printf(" %d", digit_occur[i]);

  printf("\n");
  return 0;
}
