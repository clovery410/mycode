#include <stdio.h>

int main(void)
{
  //int len;

  printf("Size of int is: %zu\n", sizeof(int));
  printf("Size of short is: %zu\n", sizeof(short));
  printf("Size of long int is: %zu\n", sizeof(long));
  printf("Size of float is: %zu\n", sizeof(float));
  printf("Size of double is: %zu\n", sizeof(double));
  printf("Size of long double is: %zu\n", sizeof(long double));

  return 0;
}
