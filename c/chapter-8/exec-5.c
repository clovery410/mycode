#include <stdio.h>

int main(void)
{
  int i, n;

  printf("Enter the length of Fibonacci numbers: ");
  scanf("%d", &n);

  int fib_numbers[n];

  for (i = 0; i < 2; i++)
    fib_numbers[i] = i;

  for (i = 2; i < n; i++) 
    fib_numbers[i] = fib_numbers[i-2] + fib_numbers[i-1];

  for (i = 0; i < n; i++)
    printf("%d ", fib_numbers[i]);

  printf("\n");

  return 0;
}
