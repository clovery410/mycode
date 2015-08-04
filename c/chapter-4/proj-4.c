#include <stdio.h>

int main(void)
{
  int num, o1, o2, o3, o4, o5;

  printf("Enter a number between 0 and 32767: ");
  scanf("%d", &num);

  o1 = num % 8;
  o2 = (num / 8) % 8;
  o3 = ((num / 8) / 8) % 8;
  o4 = (((num / 8) / 8) / 8) % 8;
  o5 = ((((num / 8) / 8) / 8) / 8) % 8;

  printf("In octal, your number is: %d%d%d%d%d\n", o5, o4, o3, o2, o1);

  return 0;
}
