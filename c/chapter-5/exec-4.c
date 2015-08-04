#include <stdio.h>

int main(void)
{
  int i, j;

  printf("Enter value of i: ");
  scanf("%d", &i);
  printf("Enter value of j: ");
  scanf("%d", &j);
  printf("Return: %d\n", (i > j) - (i < j));

  return 0;
}
