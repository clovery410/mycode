#include <stdio.h>
#include <ctype.h>

#define N 50

int main(void)
{
  int i = 0, j = 0;
  char ch, msg[N];

  printf("Enter a message: ");
  ch = getchar();
  while (ch != '\n' && i < N) {
    if (tolower(ch) >= 'a' && tolower(ch) <= 'z') {
      msg[i++] = tolower(ch);
    }
    ch = getchar();
  }

  /* Check palindrome */
  for (j = 0, i--; j < i; j++, i--) {
    if (msg[j] != msg[i]) {
      break;
    }
  }
  if (i - j > 0) {
    printf("Not a palindrome\n");
  }
  else {
    printf("Palindrome\n");
  }

  return 0;
}
