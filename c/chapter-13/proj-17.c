#include <stdio.h>
#include <ctype.h>
#include <stdbool.h>
#include <string.h>

#define N 50

bool is_palindrome(const char *message);
int read_character(char str[], int n);

int main(void)
{
  char message[N];

  printf("Enter a message: ");
  read_character(message, N);

  /* Check palindrome */
  if (is_palindrome(message))
    printf("Palindrome\n");
  else
    printf("Not a palindrome\n");

  return 0;
}

bool is_palindrome(const char *message)
{
  int i, j;

  for (i = 0, j = strlen(message) - 1; j > i; ++i, --j) {
    if (message[i] != message[j])
      break;
  }
  if (i >= j)
    return true;
  return false;
}

int read_character(char str[], int n)
{
  int ch, i = 0;

  while ((ch = getchar()) != '\n') {
    if (i < n && tolower(ch) >= 'a' && tolower(ch) <= 'z')
      str[i++] = tolower(ch);
  }
  str[i] = '\0';
  return i;
}
