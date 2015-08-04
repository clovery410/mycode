#include <stdio.h>
#include <ctype.h>

int main(void)
{
  char ch;
  int hour, minute;

  printf("Enter a 12-hour time: ");
  scanf("%d:%d %c", &hour, &minute, &ch);

  printf("Equivalent 24-hour time: ");
  switch (toupper(ch)) {
  case 'A':
    printf("%d:%d\n", hour, minute);
    break;
  case 'P':
    printf("%d:%d\n", hour + 12, minute);
  default:
    break;
  }

  return 0;
}
    
