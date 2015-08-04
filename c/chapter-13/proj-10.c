#include <stdio.h>
#include <string.h>

#define N 60

int read_line(char str[], int n);
void reverse_name(char *name);
void reverse(char* str, int start_index, int end_index);
void reverse_word(char* str);
void reverse_blank(char *str, int start_index);

int main(void)
{
  char *name;

  printf("Enter a first and last name: ");

  read_line(name, N);
  printf("Original name is \"%s\"\n", name);
  reverse_name(name);
  printf("Reversed name is \"%s\"\n", name);

  return 0;
}

void reverse_name(char *name)
{
  int i = 0, j;
  char temp;

  reverse_blank(name, 0);
  while (name[i] != ' ')
    i++;
  reverse_blank(name, i+1);
  for (i++; name[i] != ' '; ++i)
    ;
  name[i] = '\0';

  reverse_word(name);
  
  for (i = 0; name[i] != ' '; ++i)
    ;
  name[i++] = ',';
  temp = name[i];
  name[i++] = ' ';
  name[i++] = temp;
  name[i++] = '.';
  name[i] = '\0';
}

void reverse_blank(char *str, int start_index)
{
  int j = start_index;
  char temp;

  while (str[start_index] == ' ')
    start_index++;
  for (; start_index < strlen(str) - 1; ++j, ++start_index) {
    temp = str[j];
    str[j] = str[start_index];
    str[start_index] = temp;
  }
}

void reverse(char* str, int start_index, int end_index)
{
  int i,j;
  int mid_index = (start_index + end_index) / 2;
  for (i = start_index, j = end_index; i <= mid_index; ++i, --j) {
    char tmp = str[i];
    str[i] = str[j];
    str[j] = tmp;
  }
}

void reverse_word(char* str)
{
  int i_word_begin = 0, j_word_end = 0;
  reverse(str, 0, strlen(str) - 1);

  for (;;) {
    while (str[i_word_begin] == ' ')
      i_word_begin++;
    if (str[i_word_begin] == '\0')
      break;
    j_word_end = i_word_begin;
    while (str[j_word_end] != ' ' && str[j_word_end] != '\0')
      j_word_end++;
    reverse(str, i_word_begin, j_word_end - 1);
    i_word_begin = j_word_end;
  }
}

int read_line(char str[], int n)
{
  int ch, i = 0;

  while ((ch = getchar()) != '\n')
    if (i < n)
      str[i++] = ch;
  str[i] = '\0';
  return 0;
}
