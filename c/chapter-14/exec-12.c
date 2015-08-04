#include <stdio.h>

#define M 10

int main(void)
{
  #if !defined(M)
  printf("Pass\n");
  #endif

  return 0;
}
