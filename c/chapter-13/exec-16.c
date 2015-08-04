#include <stdio.h>

int count_space(const char *s)
{
  int count = 0;

  while (*s)
    if (*s++ == ' ')
      count++;
  return count;
}
