#include <stdio.h>
#include <ctype.h>
#include <stdbool.h>

#define N 20

bool are_anagrams(const char *word1, const char *word2);
int read_line(char str[], int n);

int main(void)
{
  bool result;
  char word1[N], word2[N];

  printf("Enter first word: ");
  read_line(word1, N);

  printf("Enter second word: ");
  read_line(word2, N);

  result = are_anagrams(word1, word2);
  printf("The words are ");
  if (!result)
    printf("not ");
  printf("anagrams.\n");

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

bool are_anagrams(const char *word1, const char *word2)
{
  int i = 0, j = 0, letter[26] = {0};

  while (word1[i]) {
    letter[tolower(word1[i]) - 'a']++;
    i++;
  }

  while (word2[j]) {
    letter[tolower(word2[j]) - 'a']--;
    j++;
  }

  for (i = 0; i < 26; i++) {
    if (letter[i] != 0) {
      return false;
    }
  }
  return true;
}
