#include <stdio.h>
#include <string.h>

#define N 50

void reverse(char *message);
int read_line(char str[], int n);

int main(void)
{
  char mess[N];

  /* Read message, and put it in the array */
  printf("Enter a message: ");
  read_line(mess, N);

  /* Reverse the message */
  reverse(mess);

  /* print the reversed message*/
  printf("Reversal is: %s\n", mess);
  
  return 0;
}

void reverse(char *message)
{
  char temp, *begin, *end;

  begin = message;
  end = message + strlen(message) - 1;

  while (begin < end) {
    temp = *begin;
    *begin++ = *end;
    *end-- = temp;
  }
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
