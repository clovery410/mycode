#include <stdio.h>
#include <string.h>

//#define LEN_DOMAIN 100
#define LEN_URL 200

void build_index_url(const char *domain, char *index_url);

int main(void)
{
  const char domain[] = "knking.com";
  char index_url[LEN_URL];
  build_index_url(domain, index_url);
  printf("%s\n", index_url);

  return 0;
}

void build_index_url(const char *domain, char *index_url)
{
  strcpy(index_url, "http://www.");
  strcat(index_url, domain);
  strcat(index_url, "/index.html");
}
