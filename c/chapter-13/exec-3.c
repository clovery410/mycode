#include <stdio.h>

int main(void)
{
  int i, j;
  char *s;

  printf("Enter: ");
  scanf("%d%s%d", &i, s, &j);

  printf("%d\n", i);
  //printf("%s\n", s);
  // printf("%d\n", j);

  return 0;
}
