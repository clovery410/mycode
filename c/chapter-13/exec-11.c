#include <stdio.h>

#define N 60

int my_strcmp(char *s, char *t);

int main(void)
{
  char *s = "Hello";
  char *t = "hello";

  if (my_strcmp(s, t) > 0)
    printf("%s bigger than %s\n", s, t);
  else if (my_strcmp(s, t) == 0)
    printf("%s and %s are equal\n", s, t);
  else
    printf("%s smaller than %s\n", s, t);
}

int my_strcmp(char *s, char *t)
{
  int i;

  for (i = 0; *(s + i) == *(t + i); i++) {
    if (*(s + i) == '\0')
      return 0;
  }
  return *(s + i) - *(t + i);
}
