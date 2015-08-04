#include <stdio.h>

int num_digits(int n);

int main(void)
{
  int n;

  printf("Enter a number: ");
  scanf("%d", &n);
  printf("The number of digits in %d is %d\n", n, num_digits(n));

  return 0;
}

int num_digits(int n)
{
  int num = 0;
  while (n > 0) {
    num++;
    n = n / 10;
  }
  return num;
}

