#include <stdio.h>
#include <ctype.h>

#define N 50

int main(void)
{
  char ch, msg[N], *p, *q;

  p = &msg[0];
  q = &msg[0];
  printf("Enter a message: ");
  ch = getchar();
  while (ch != '\n' && p < &msg[N]) {
    if (tolower(ch) >= 'a' && tolower(ch) <= 'z') {
      *p++ = tolower(ch);
    }
    ch = getchar();
  }

  for (--p; p > q; q++, p--) {
    if (*q != *p) {
      break;
    }
  }
  
  if (p > q) {
    printf("Not a palindrome\n");
  }
  else {
    printf("Palindrome\n");
  }

  return 0;
}
