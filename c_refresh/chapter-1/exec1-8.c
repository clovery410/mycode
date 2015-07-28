#include <stdio.h>

int main(void)
{
  long c, ns, nt, nr;
  ns = nt = nr = 0;

  while ((c = getchar()) != EOF)
    {
      if (c == ' ')
	++ns;
      else if (c == '\t')
	++nt;
      else if (c == '\n')
	++nr;
    }

  printf("Space: %ld\nTab: %ld\nReturn: %ld\n", ns, nt, nr);
  
  return 0;
}
