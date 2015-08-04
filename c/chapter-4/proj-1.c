#include <stdio.h>

int main(void)
{
  int i, j, num;
  
  printf("Enter a two-digit number: ");
  scanf("%d", &num);
  
  i = num / 10;
  j = num % 10;
  
  printf("The reversal is: %d\n", j * 10 + i);

  return 0;
}
