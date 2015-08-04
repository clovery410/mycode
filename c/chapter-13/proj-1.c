#include <stdio.h>
#include <string.h>

#define LEN_WORD 20

int read_line(char str[], int n);

int main(void)
{
  int n;
  char smallest_word[LEN_WORD+1], largest_word[LEN_WORD+1], input[LEN_WORD+1];

  printf("Enter word: ");
  read_line(input, LEN_WORD);
  strcpy(smallest_word, input);
  strcpy(largest_word, input);
  
  for (;;) {
    printf("Enter word: ");
    n = read_line(input, LEN_WORD);
    if (n == 4)
      break;
    else if (strcmp(input, smallest_word) < 0)
      strcpy(smallest_word, input);
    else if (strcmp(input, largest_word) > 0)
      strcpy(largest_word, input);
  }
  printf("Smallest word: %s\n", smallest_word);
  printf("Largest word: %s\n", largest_word);

  return 0;
}

int read_line(char str[], int n)
{
  int ch, i = 0;

  while ((ch = getchar()) != '\n')
    if (i < n)
      str[i++] = ch;
  str[i] = '\0';
  return i;
}
