#include <stdio.h>

int fact(int n);

int main(void)
{
  int n;
  
  printf("Enter number: ");
  scanf("%d", &n);

  printf("Factorial of %d is %d\n", n, fact(n));

  return 0;
}

int fact(int n)
{
  int result;

  for (result = 1; n > 1; n--)
    result *= n;

  return result;
}
