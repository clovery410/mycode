#include <stdio.h>

#define LEN 100

/* count the number of all characters that between ASCII ! to ASCII ~ (33-126) */
int main(void)
{
  int c, i, j;
  int num[LEN];

  for (i = 0; i < LEN; ++i)
      num[i] = 0;

  while ((c = getchar()) != EOF)
    {
      if (c < '!' || c > '~')
	;
      else
	++num[c - '!'];
    }

  for (i = 0; i < ('~' - '!'); ++i)
    {
      if (num[i] != 0)
	{
	  printf("%c: ", '!' + i);
	  for (j = num[i]; j > 0; --j)
	    printf("*");
	  printf("\n");
	}
    }

  return 0;
}
