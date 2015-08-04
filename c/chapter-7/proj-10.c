#include <ctype.h>
#include <stdio.h>

int main(void)
{
  char ch;
  int num = 0;

  printf("Enter a sentence: ");
  
  while((ch = getchar()) != '\n') {
    switch (tolower(ch)) {
    case 'a': case 'e': case 'i': case 'o': case 'u':
      num ++;
      break;
    default:
      break;
    }
  }
  printf("Your sentence contains %d vowels.\n", num);

  return 0;
}
