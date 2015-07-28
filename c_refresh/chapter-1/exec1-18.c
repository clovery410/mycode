#include <stdio.h>
#define MAXLINE 1000

void getdoc(char line[], int maxline);

int main (void)
{
  char doc[MAXLINE];

  getdoc(doc, MAXLINE);
  printf("%s", doc);

  return 0;
}

void getdoc(char s[], int lim)
{
  int c, i;

  for (i = 0; i < lim - 1 && (c = getchar()) != EOF; ++i)
    {
      s[i] = c;
      if (s[0] == '\n' || s[i] == '\t')
	--i;
      else if (s[i-1] == '\n' && s[i] == '\n')
	--i;
      else if (s[i-1] == ' ' && s[i] == '\n')
	{
	  s[i-1] = '\n';
	  --i;
	}
      
    }
  s[i] = '\0';
}
