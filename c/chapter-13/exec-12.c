#include <stdio.h>
#include <string.h>

#define N 60

void get_extension(const char *file_name, char *extension);

int main(void)
{
  const char *file_name = "memo.txt";
  char extension[N];
  get_extension(file_name, extension);

  printf("%s\n", extension);
  return 0;
}

void get_extension(const char *file_name, char *extension)
{
  int i = 0;
  while (i < strlen(file_name)) {
    if (file_name[i++] == '.')
      break;
  }
  strcpy(extension, file_name + i);
}
