#include <stdio.h>

#define N 50

int main(void)
{
  char msg[N], *p
  
  printf("Enter a message: ");
  for (p = msg; p < msg + N; p++) {
    *p = getchar();
    if (*p == '\n') {
      break;
    }
  }

  printf("Reversal is: ");
  for (--p; p >= msg; p--) {
    putchar(*p);
  }
  putchar('\n');

  return 0;
}
