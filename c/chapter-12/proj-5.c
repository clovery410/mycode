#include <stdio.h>

#define LEN 50

int main(void)
{
  char ch, sen[LEN] = {' '}, *p, *q;
  int i;

  printf("Enter a sentence: ");
  
  for (p = &sen[1]; p < &sen[LEN]; p++) {
    ch = getchar();
    if (ch == '?' || ch == '!')
      break;
    *p = ch;
  }

  printf("Reversal of sentence:");
  for (q = p; q >= &sen[0]; q--) {
    if (*q == ' ') {
      for (i = 0; i <= p - q; i++)
	printf("%c", *(q + i));
      p = q - 1;
    }
  }

  printf("%c\n", ch);

  return 0;
}
