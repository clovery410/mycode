#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
  FILE * fp;
  char * line = NULL;
  size_t len = 0;
  ssize_t read;

  fp = fopen("/Users/admin/Learn/c_refresh/kargerMinCut.txt", "r");
  if (fp == NULL)
    exit(EXIT_FAILURE);

  while ((read = getline(&line, &len, fp)) != -1) {
    char *token, *string, *tofree;

    tofree = string = strdup(line);

    while ((token = strsep(&string, "\t")) != NULL)
      printf("%d\n", atoi(token));

    free(tofree);
  }

  fclose(fp);
  if (line)
    free(line);

  exit(EXIT_SUCCESS);
}
