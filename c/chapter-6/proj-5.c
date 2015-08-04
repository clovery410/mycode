#include <stdio.h>

int main(void)
{
  int n;

  printf("Enter a digit number: ");
  scanf("%d", &n);

  printf("The reversed number is: ");
  do {
    printf("%d", n % 10);
    n /= 10;
  } while (n != 0);
  
  printf("\n");
  return 0;
}
