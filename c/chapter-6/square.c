/* Prints a table of squares using a while statement */

#include <stdio.h>

int main(void)
{
  int n, i;
  i = 1;

  printf("This program prints a table of squares.\nEnter number of entries in table: ");
  scanf("%d",&n);

  while (i <= n) {
    printf("%10d%10d\n", i, i * i);
    i++;
  }

  return 0;
}
