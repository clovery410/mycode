#include <stdio.h>

int main(void)
{
  int n, m = 10;

  /* for (n = 0; m > 0; n++) { */
  /*   m /= 2; */
  /*   printf("%d ", m + n); */
  /* } */

  for (n = 0; m > 0; n++, m /= 2)
    printf("%d ", m + n);

  return 0;
}
