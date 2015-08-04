/* Please see Project 2 in Chapter 11 for better expression */

#include <stdio.h>

int main(void)
{
  int hour, minute, time;
  
  printf("Enter a 24-hour time: ");
  scanf("%d:%d", &hour, &minute);

  printf("Closest departure time is ");
  time = hour * 60 + minute;
  
  if (time <= 307 || time >= 1222 )
    printf("9:45 p.m., arriving at 11:58 p.m.\n");
  else if (time < 531)
    printf("8:00 a.m., arriving at 10:16 a.m.\n");
  else if (time < 631)
    printf("9:43 a.m., arriving at 11:52 a.m.\n");
  else if (time < 723)
    printf("11:19 a.m., arriving at 1:31 p.m.\n");
  else if (time < 803)
    printf("12:47 p.m., arriving at 3:00 p.m.\n");
  else if (time < 892)
    printf("2:00 p.m., arriving at 4:08 p.m.\n");
  else if (time < 1042)
    printf("3:45 p.m., arriving at 5:55 p.m.\n");
  else if (time < 1222)
    printf("7:00 p.m., arriving at 9:20 p.m.\n");

  return 0;
}
