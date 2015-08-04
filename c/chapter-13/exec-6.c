#include <stdio.h>

#define N 60

int read_line(char str[], int n);
void censor(char str[]);

int main(void)
{
  char rep_str[N];
  int n;

  printf("Enter something: ");
  n = read_line(rep_str, N);
  censor(rep_str);
  printf("%s\n", rep_str);

  return 0;
}

int read_line(char str[], int n)
{
  int ch, i = 0;

  while ((ch = getchar()) != '\n') {
    if (i < n)
      str[i++] = ch;
  }
  str[i] = '\0';
  return i;
}

void censor(char str[])
{
  int i = 0;

  for (i = 0; str[i] != '\0', i++) {
    if (str[i] == 'f' && str[i+1] == 'o' && str[i+2] == 'o') {
      str[i] = 'x';
      str[i+1] = 'x';
      str[i+2] = 'x';
    }
  }
}
