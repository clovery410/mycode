#include <ctype.h>
#include <stdio.h>

#define LEN 60

int read_line(char str[], int n);
int compute_vowel_count(const char *sentence);

int main(void)
{
  char str[LEN];

  printf("Enter a sentence: ");
  read_line(str, LEN);
  printf("Your sentence contains %d vowels.\n", compute_vowel_count(str));

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

int compute_vowel_count(const char *sentence)
{
  int i = 0, num = 0;

  while (sentence[i]) {
    switch (tolower(sentence[i++])) {
    case 'a': case 'e': case 'i': case 'o': case 'u':
      num ++;
      break;
    }
  }
  return num;
}
