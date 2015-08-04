/* Determines the length of a message */

#include <stdio.h>

int main(void)
{
  int length = 0;

  printf("Enter a message: ");
 
  while (getchar() != '\n') 
    length ++;

  printf("Your message was %d character(s) long.\n", length);

  return 0;
}
