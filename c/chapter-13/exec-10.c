#include <stdio.h>
#include <string.h>

#define LEN 100

char *duplicate(char *q, const char *p);

int main(void)
{
  char str2[LEN + 1];
  const char str[] = "Hello world!";
  duplicate(str2, str);
  /* printf("Address of str: %x\n", str);*/
  // printf("%s\n", str);
   printf("%s\n", str2);
  /*printf("%s\n", str);*/
  
  return 0;
}
char *duplicate(char *q, const char *p)
{
  //  char str[LEN+1], *q;
  //char str2[100];
  //q = str;

  strcpy(q, p);
  //strcpy(str2, p);
  /*printf("Address of q: %x\n", q);*/
  return q;
}
