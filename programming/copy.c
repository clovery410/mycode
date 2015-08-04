#include <stdio.h>

main()
{

  int c, has_space;
  
  has_space = 0;
  while ((c = getchar()) != EOF)
    {
      if (c == ' ')

	has_space = 1;
      else {
	if (has_space != 0) {
	  printf("*");
	  --has_space;
	}
	printf("%c", c);
      }
    }
  if ( has_space != 0)
    printf("*");
  return 0;
}
