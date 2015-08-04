#include <stdio.h>

int main(void)
{
  int n;
  n = 0;

  if (n >= 1 <= 10)
    printf("n is between 1 and 10\n");

  return 0;
}

/* This if statement is legal but makes no sense, since (n >= 1 <= 10) will first evaluate n >= 1, result is a boolean value either 1 or 0. It then evaluated (result) <= 10, sicne result is either 1 or 0, so this statement would always return 1 */
