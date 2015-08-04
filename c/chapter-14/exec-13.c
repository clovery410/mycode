#include <stdio.h>

#define N 100

void f(void);

int main(void)
{
  f();
#ifdef N
#undef N
#endif
  return 0;
}

void f(void)
{
#if defined(N)
  printf("N is %d\n", N);
#else
  printf("N is undefined\n");
#endif
}

/***************************
Lines brought in from stdio.h
Blank line
Blank line
Blank line
void f(void);
Blank line
void main(void)
{
  f();
  return 0;
}
Blank line
void f(void)
{
  printf("N is undefined\n");
}
****************************/
