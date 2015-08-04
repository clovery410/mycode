#include <stdio.h>

int main(void)
{
  char first, ch;

  printf("Enter a first and last name: ");

  while ((first = getchar()) == ' ')
    ;
  while (getchar() != ' ')
    ;
  while ((ch = getchar()) == ' ')
    ;
  putchar(ch);
  while ((ch = getchar()) != '\n') {
    if (ch == ' ')
      ;
    else
      putchar(ch);
  }

  printf(", %c.\n", first);

  return 0;
}
      
      
  
