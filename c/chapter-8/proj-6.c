#include <stdio.h>
#include <ctype.h>

#define N 50
//#define LENGTH ((int) (sizeof(biff) / sizeof(biff[0])))

int main(void)
{
  char ch, biff[N];
  int j, i = 0;

  printf("Enter message: ");

  while ((ch = getchar()) != '\n') {
    biff[i] = ch;
    i++;
  }

  printf("In B1FF-speak: ");

  for (j = 0; j < i; j++) {
    switch (toupper(biff[j])) {
    case 'A': printf("4"); break;
    case 'B': printf("8"); break;
    case 'E': printf("3"); break;
    case 'I': printf("1"); break;
    case 'O': printf("0"); break;
    case 'S': printf("5"); break;
    default: printf("%c", toupper(biff[j])); break;
    }
  }

  printf("!!!!!!!!!!\n");

  return 0;
}
