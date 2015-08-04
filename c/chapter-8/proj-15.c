#include <stdio.h>

#define LEN 80

int main(void)
{
  char ch, message[LEN];
  int i, j, n;

  printf("Enter message to be encrypted: ");
  for (i = 0; i < LEN; i++) {
    ch = getchar();
    if (ch == '\n')
      break;
    else
      message[i] = ch;
  }

  printf("Enter shift amount (1-25): ");
  scanf("%d", &n);

  printf("Encrypted message: ");
  for (j = 0; j < i; j++) {
    if (message[j] >= 'A' && message[j] <= 'Z')
      printf("%c", ((message[j] - 'A') + n) % 26 + 'A');
    else if (message[j] >= 'a' && message[j] <= 'z')
      printf("%c", ((message[j] - 'a') + n) % 26 + 'a');
    else
      printf("%c", message[j]);
  }

  printf("\n");
  return 0;
}
