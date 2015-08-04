#include <stdio.h>

#define N 10

int read_line(char str[], int n);

int main(void)
{
  char msg_str[N];
  
  printf("Enter something: ");

  read_line(msg_str, N);
  printf("%s\n", msg_str);

  return 0;
}

int read_line(char str[], int n)
{
  int ch, i = 0;

  while ((ch = getchar()) == ' ')
    ;
  while (ch != '\n') {
    if (i < n) {
      str[i++] = ch;
    }
    ch = getchar();
  }
  str[i] = '\0';
  return i;
}
