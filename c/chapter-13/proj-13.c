#include <stdio.h>

#define LEN 80

void encrypt(char *message, int shift);
int read_line(char str[], int n);

int main(void)
{
  char message[LEN];
  int i, j, n;

  printf("Enter message to be encrypted: ");
  read_line(message, LEN);

  printf("Enter shift amount (1-25): ");
  scanf("%d", &n);

  encrypt(message, n);
  printf("Encrypted message: %s\n", message);

  return 0;
}

void encrypt(char *message, int shift)
{
  int i = 0;

  while (message[i]) {
    if (message[i] >= 'A' && message[i] <= 'Z') {
      message[i] = ((message[i] - 'A') + shift) % 26 + 'A';
      i++;
    }
    else if (message[i] >= 'a' && message[i] <= 'z') {
      message[i] = ((message[i] - 'a') + shift) % 26 + 'a';
      i++;
    }
    else
      i++;
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
