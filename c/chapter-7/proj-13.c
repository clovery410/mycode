#include <stdio.h>

int main(void)
{
  int num = 0, begin = 0;
  float len = 0.0;
  char ch;

  printf("Enter a sentence: ");
  
  while ((ch = getchar()) != '\n') {
    if (ch == ' ' && len == 0.0)
      ;
    else if (ch != ' ' && begin == 0) {
      len++;
      num++;
      begin = 1;
    }
    else if (ch != ' ')
      len++;
    else if (ch == ' ')
      begin = 0;
  }

  printf("Average word length: %.1f\n", len / num);

  return 0;
}
      
