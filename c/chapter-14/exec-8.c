#include <stdio.h>

#define S1(x) #x
#define S2(x) S1(x)
#define LINE_FILE "Line " S2(__LINE__) " of file " __FILE__

int main(void)
{
  const char *str = LINE_FILE;
  printf("%s\n", str);

  return 0;
}
