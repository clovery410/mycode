#include <stdio.h>

int main(void)
{
  int hour, minute;

  printf("Enter a 24-hour time: ");
  scanf("%d:%d", &hour, &minute);

  printf("Equivalent 12-hour time: ");
  if (hour == 0)
    printf("12:%.2d AM\n", minute);
  else if (hour < 12)
    printf("%d:%.2d AM\n", hour, minute);
  else if (hour == 12)
    printf("%d:%.2d PM\n", hour, minute);
  else 
    printf("%d:%.2d PM\n", hour - 12, minute);

  return 0;
}
