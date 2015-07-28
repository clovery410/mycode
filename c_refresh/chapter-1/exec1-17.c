#include <stdio.h>
#define MAXLINE 1000

int getlength (char line[], int maxline);
//void copy (char to[], char from[]);

int main (void)
{
  int len;
  //  int max;
  char line[MAXLINE];
  //  char longer[MAXLINE];

  //max = 0;
  while ((len = getlength(line, MAXLINE)) > 0)
    if (len > 80)
      printf("%s", line);

  return 0;
}

int getlength (char s[], int lim)
{
  int c, i;

  for (i = 0; i < lim - 1 && (c = getchar()) != EOF && c != '\n'; ++i)
    s[i] = c;

  if (c == '\n')
    {
      s[i] = c;
      ++i;
    }
  s[i] = '\0';
  return i;
}
