#include <stdio.h>
#include <limits.h>

int main (void)
{
  printf("signed char: %d ~ %d\n", SCHAR_MIN, SCHAR_MAX);
  printf("unsigned char max: %d\n", UCHAR_MAX);
  printf("signed short: %d ~ %d\n", SHRT_MIN, SHRT_MAX);
  printf("unsigned short max: %d\n", USHRT_MAX);
  printf("signed int: %d ~ %d\n", INT_MIN, INT_MAX);
  printf("unsigned int max: %u\n", UINT_MAX);
  printf("signed long: %ld ~ %ld\n", LONG_MIN, LONG_MAX);
  printf("unsigned long max: %lu\n", ULONG_MAX);
  printf("signed long long: %lld ~ %lld\n", LLONG_MIN, LLONG_MAX);
  printf("char: %d ~ %d\n", CHAR_MIN, CHAR_MAX);

  return 0;
}
