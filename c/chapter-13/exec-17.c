#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <ctype.h>

#define LEN 100

bool test_extension(const char *file_name, const char *extension);

int main(void)
{
  const char *file_name = "memo.txt";
  const char *extension = "TXT";
  if (test_extension(file_name, extension))
    printf("extension is right\n");
  else
    printf("extension is wrong\n");

  return 0;
}

bool test_extension(const char *file_name, const char *extension)
{
  char *p = file_name;
  char *q = extension;

  while (*p) {
    if (*p++ == '.')
      break;
  }
  while (*p || *q) {
    if (toupper(*p++) != toupper(*q++))
      return false;
  }
  return true;
}
