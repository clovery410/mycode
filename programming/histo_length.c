#include <stdio.h>

main()
{

  int c, i, nlength;
  
  nlength = 0;

  printf ("Please input several words, use blabk to seprarte them:\n");
  while ((c = getchar()) != EOF)
    {
      if (c != ' ')
	{
          printf ("%c",c);
          ++nlength;
	}
      else if (c == ' ')
	{
          printf ("|");
	  for (i=0; i < nlength; ++i)
	    printf ("*");
          printf ("\n");
          nlength = 0;
	}
    }
}
