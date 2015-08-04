#include <stdio.h>
#include <string.h>

#define N 60

int main(void)
{
  char str[N];
  strcpy(str, "tire_bouchon");
  strcpy(&str[4], "d-or-wi");
  strcat(str, "red?");

  printf("%s\n", str);

  return 0;
}
