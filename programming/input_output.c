#include <stdio.h>
main()
{
  char c;

  while ((c = getchar()) != EOF)
    {
      printf ("%c\n", c);
    }
}
