#include <stdio.h>
#include <string.h>

#define N 60

int main(void)
{
  char s1[N], s2[N];
  strcpy(s1, "computer");
  strcpy(s2, "science");
  if (strcmp(s1, s2) < 0)
    strcat(s1, s2);
  else
    strcat(s2, s1);
  s1[strlen(s1) - 6] = '\0';
  printf("%s\n", s1);
  
  return 0;
}
