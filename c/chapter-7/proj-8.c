#include <stdio.h>
#include <ctype.h>

int main(void)
{
  int hour, minute, time;
  char ch;

  printf("Enter a 12-hour time: ");
  scanf("%d:%d %c", &hour, &minute, &ch);

  printf("Closest departure time is ");
  switch (toupper(ch)) {
  case 'A':
    time = hour * 60 + minute;
    break;
  case 'P': 
    time = (hour + 12) * 60 + minute;
    break;
  default:
    printf("Please enter the AM/PM indicator");
    break;
  }
  
  if (time <= 307 || time >= 1222 )    printf("9:45 p.m., arriving at 11:58 p.m.\n");
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
