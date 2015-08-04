#include <stdio.h>
#include <string.h>

#define TOUPPER(c) ('a' <= (c) && (c) <= 'z' ? (c) - 'a' + 'A': (c))

int main(void)
{
  int i;
  char *s;

  strcpy(s, "0123");
  i = 0;
  putchar(TOUPPER(s[++i]));

  return 0;
}
