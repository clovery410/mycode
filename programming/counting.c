#include <stdio.h>

/* count characters in input; 1st version */
main()
{
 
  int nc;
  nc = 0;
  while (getchar() != EOF)
       ++nc;
  printf("%d\n", nc);
}
