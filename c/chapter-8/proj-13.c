#include <stdio.h>

#define LEN_NAME 50

int main(void)
{
  char first, ch, last_name[LEN_NAME];
  int i, j;

  printf("Enter a first and last name: ");

  scanf(" %c", &first);

  while ((ch = getchar()) != ' ')
    ;
  for (i = 0; i < LEN_NAME && ch != '\n'; i++) {
    last_name[i] = ch;
    ch = getchar();
  }

  printf("You entered the name: ");
  for (j = 0; j < i; j++)
    printf("%c", last_name[j]);

  printf(", %c.\n", first);

  return 0;
}
