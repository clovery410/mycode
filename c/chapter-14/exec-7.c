#include <stdio.h>

#define GENERIC_MAX(type)          \
type type##_max(type x, type y)    \
{                                  \
  return x > y ? x : y;            \
}

typedef unsigned long ULONG;

GENERIC_MAX(long);
GENERIC_MAX(ULONG);

int main(void)
{
}
/*
long long_max(long x, long y)
{
  return x > y ? x : y;
}

ULONG ULONG_max(ULONG x, ULONG y)
{
  return x > y ? x : y;
}
*/
