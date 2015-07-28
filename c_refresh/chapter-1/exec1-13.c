#include <stdio.h>

#define LEN 20
int main(void)
{
  int c, i, j, k;
  int word[LEN];

  for (i = 0; i < LEN; ++i)
    word[i] = 0;

  i = 0;
  while ((c = getchar()) != EOF)
    {
      if (i >= LEN)
	{
	  printf("Too many words!\n");
	  return 0;
	}
      
      if (c == ' ' || c == '\t' || c == '\n')
	++i;
      else if ((c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z'))
	++word[i];
    }

  for (j = 0; j < i; ++j)
    {
      for (k = word[j]; k > 0; --k)
	printf("*");
      printf("\n");
    }

  return 0;
}
