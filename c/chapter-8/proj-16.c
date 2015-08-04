#include <stdio.h>
#include <ctype.h>

int main(void)
{
  int i;
  int letter[26] = {0};
  char ch;

  printf("Enter first word: ");
  while ((ch = getchar()) != '\n') {
    if (tolower(ch) >= 'a' && tolower(ch) <= 'z')
      letter[(tolower(ch) - 'a')] += 1;
  }

  printf("Enter second word: ");
  while ((ch = getchar()) != '\n') {
    if (tolower(ch) >= 'a' && tolower(ch) <= 'z')
      letter[(tolower(ch) - 'a')] -= 1;
  }

  printf("The words are ");
  for (i = 0; i < 26; i++) {
    if (letter[i] != 0) {
      printf("not ");
      break;
    }
  }
  printf("anagrams.\n");

  return 0;
}
