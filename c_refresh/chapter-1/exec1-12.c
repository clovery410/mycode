#include <stdio.h>

//#define IN 1
//#define OUT 0

int main(void)
{
  int c;

  while ((c = getchar()) != EOF)
    {
      if (c == ' ')
	putchar('\n');
      else
	putchar(c);
    }
  
  return 0;
}
