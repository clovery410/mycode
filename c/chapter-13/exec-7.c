#include <stdio.h>
#include <string.h>

#define N 10

int main(void)
{
  char str[N] = {'a', 'c', 'd', 'e'};
  *str = 0;
  //str[0] = '\0';
  //strcpy(str, "");
  //strcat(str, "");
  printf("%s\n", str);

  return 0;
}
