#include <stdio.h>
#include <string.h>

void remove_filename(char *url);

int main(void)
{
  char url[] = "http://www.knking.com/index.html";
  remove_filename(url);
  printf("%s\n", url);

  return 0;
}

void remove_filename(char *url)
{
  int i;
  i = strlen(url) - 1;

  while (url[i] != '/') {
    i--;
  }
  strcpy(&url[i], "");
}
