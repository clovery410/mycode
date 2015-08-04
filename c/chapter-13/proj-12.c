#include <stdio.h>

#define LEN_WORD 20
#define NUM_WORD 30

int read_line(char sentence[][LEN_WORD], int n);

int main(void)
{
  int i, n;
  char sentence[NUM_WORD][LEN_WORD];
  
  printf("Enter a sentence: ");
  n = read_line(sentence, NUM_WORD);

  printf("Reversal of sentence: ");
  for (i = n; i >= 0; --i) {
    printf("%s ", sentence[i]);
  }
  printf("\n");

  return 0;
}

int read_line(char sentence[][LEN_WORD], int n)
{
  int ch, i = 0, j = 0;

  for (i = 0; i < n; i++) {
    j = 0;
    while ((ch = getchar()) != ' ' && ch != '\n')
      sentence[i][j++] = ch;
    sentence[i][j] = '\0';
    if (ch == '\n')
      break;
  }
  return i;
}
