#include <stdio.h>

int main(void)
{
  int c, n;
  int i = 0;

  while ((c = getchar()) != EOF)
    {
      if (c == ' ' && i == 1)
	;
      else if (c == ' ' && i == 0)
	{
	  putchar(c);
	  i = 1;
	}
      else
	{
	  putchar(c);
	  i = 0;
	}
    }
  printf("\n");
  return 0;
}
