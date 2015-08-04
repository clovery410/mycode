#include <stdio.h>

#define N 10

int read_line(char str[], int n);

int main(void)
{
  char msg_str[N];

  while (1) {
  printf("Enter something: ");
  read_line(msg_str, N);
  printf("%s\n", msg_str);
  }

  return 0;
}

int read_line(char str[], int n)
{
  int ch, i = 0;

  for (i = 0; i < n; i++) {
    ch = getchar();
    if (ch == '\n')
      break;
    str[i] = ch;
  }
  str[i] = '\0';
  return i;
}
