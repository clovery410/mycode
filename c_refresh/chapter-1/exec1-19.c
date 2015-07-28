#include <stdio.h>
#define MAX 1000

int origin (char line[], int lim);
void reverse (char old[], char new[], int len);

int main (void)
{
  char line[MAX];
  char reline[MAX];
  int length;

  length = origin(line, MAX);
  reverse(line, reline, length);
  printf("%s\n", reline);

  return 0;
}

int origin (char s[], int lim)
{
  int c, i;

  for (i = 0; i < lim - 1 && (c = getchar()) != EOF && c != '\n'; ++i)
      s[i] = c;
  s[i] = '\0';

  return i;
}

void reverse (char s[], char new_s[], int len)
{
  int i;

  for (i = 0; i < len; ++i)
    {
      new_s[i] = s[len -1 - i];
    }
}
