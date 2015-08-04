#include <stdio.h>

#define N 60

double compute_average_word_length(const char * sentence);
int read_line(char str[], int n);

int main(void)
{
  char *sentence;
  printf("Enter a sentence: ");

  read_line(sentence, N);

  printf("Average word length: %lf\n", compute_average_word_length(sentence));

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

double compute_average_word_length(const char *sentence)
{
  int i, num = 0;
  double length = 0.0;

  for (i = 0; sentence[i] != '\0'; i++) {
    if (sentence[i] == ' ')
      num++;
    else if (sentence [i] != ' ')
      length++;
  }
  return length / (num + 1);
}
