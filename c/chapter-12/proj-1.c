#include <stdio.h>

#define N 50

int main(void)
{
  char ch, *p, mess[N];

  /* Read message, and put it in the array */
  p = mess;
  printf("Enter a message: ");
  ch = getchar();
  while (ch != '\n' && p < mess + N) {
    *p++ = ch;
    ch = getchar();
  }

  /* print in reversal */
  printf("Reversal is: ");
  while (p >= mess) {
    printf("%c", *p);
    p--;
  }
  printf("\n");
  
  return 0;
}
