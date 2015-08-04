#include <stdio.h>

main()
{
  int c, nb;

  nb = 0;
  while ((c = getchar()) != EOF){
	 if (c == ' ')
	   nb = nb + 1;
    }
   printf ("%d\n", nb);
}
