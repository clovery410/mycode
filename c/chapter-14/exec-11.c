#include <stdio.h>

#define ERROR(index) fprintf(stderr, "Range error: index = %d\n", index)

int main(void)
{
  int index = 2;
  ERROR(index);

  return 0;
}
