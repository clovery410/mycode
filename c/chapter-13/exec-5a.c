#include <stdio.h>
#include <ctype.h>

#define N 60

void capitalize (char str[], int n);
int read_line(char str[], int n);

int main(void) {
  char cap_str[N];
  int n;

  printf("Enter something: ");
  n = read_line(cap_str, N);
  capitalize(cap_str, n);
  printf("%s\n", cap_str);

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

void capitalize (char str[], int n)
{
  int i;

  for (i = 0; i < n; i++){
    if (str[i] >= 'a' && str[i] <= 'z')
      str[i] = toupper(str[i]);
  }
}
