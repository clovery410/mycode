#include <stdio.h>

#define LEN 50

int main(void)
{
  char ch, sentence[LEN] = {' '};
  int i, j, k;

  printf("Enter a sentence: ");
  
  for (i = 1; i < LEN; i++) {
    ch = getchar();
    if (ch == '?' || ch == '!')
      break;
    sentence[i] = ch;
  }

  printf("Reversal of sentence:");
  for (j = i - 1; j >= 0; j--) {
    if (sentence[j] == ' ') {
      for (k = j; k < i; k++)
	printf("%c", sentence[k]);
      i -= i - j;
    }
  }

  printf("%c\n", ch);

  return 0;
}
