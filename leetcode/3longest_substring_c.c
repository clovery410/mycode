#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int lengthOfLongestSubstring(char* s) {
  int i, j, longest;
  int a[128] = {0};
  int begin = 0;
  longest = 0;

  if (strlen(s) <= 1)
    return strlen(s);

  while (s[begin] == s[0]) {
    a[s[0]]++;
    begin++;
  }
      
  for (i = begin - 1, j = begin; s[j] != '\0' && s[i] != '\0'; j++) {
    if (a[s[j]] >= 1) {
      if (j - i > longest)
	longest = j - i;
      while (s[i] != s[j]) {
	a[s[i]] = 0;
	i++;
      }
      i++;
    }
    else
      a[s[j]]++;
  }

  if (j - i > longest)
    longest = j - i;

  return longest;
}

int main(void) {
  //  char *s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+abcdefggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg";
  char *s = "ggububgvfk";
  int len;

  len = lengthOfLongestSubstring(s);
  printf("%d\n", len);
  return 0;
}
  

