#include <stdio.h>
#include <ctype.h>
#include <string.h>

#define LEN 60

int read_line(char str[], int n);
int compute_scrabble_value(const char *word);

int main(void)
{
  char str[LEN];

  printf("Enter a word: ");
  read_line(str, LEN);
  
  printf("Scrabble value: %d\n", compute_scrabble_value(str));
  
  return 0;
}

int compute_scrabble_value(const char *word)
{
  int i = 0, sum = 0;

  while (word[i]) {
    switch (toupper(word[i++])) {
    case 'A': case 'E': case 'I': case 'L': case 'N': case 'O': case 'R': case 'S': case 'T': case 'U':
      sum += 1;
      break;
    case 'D': case 'G':
      sum += 2;
      break;
    case 'B': case 'C': case 'M': case 'P':
      sum += 3;
      break;
    case 'F': case 'H': case 'V': case 'W': case 'Y':
      sum += 4;
      break;
    case 'K':
      sum += 5;
      break;
    case 'J': case 'X':
      sum += 8;
      break;
    case 'Q': case 'Z':
      sum += 10;
      break;
    default:
      break;
    }
  }
  return sum;
}

int read_line(char str[], int n)
{
  int ch, i = 0;

  while ((ch = getchar()) != '\n'){
    if (i < n)
      str[i++] = ch;
  }
  str[i] = '\0';
  return i;
}
