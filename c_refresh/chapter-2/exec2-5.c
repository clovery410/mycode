#include <stdio.h>

int any (char s1[], char s2[]);

int main (void)
{
  char str1[] = "abce";
  char str2[] = "cedi";

  printf("The position is %d\n", any(str1, str2));

  return 0;
}

int any (char s1[], char s2[])
{
  int i, j, k, p;

  p = -1;
  for (i = 0; s1[i] != '\0'; i++)
    {
      for (j = 0; (s2[j] != '\0') && (s1[i] != s2[j]); j++)
	;
      if (s2[j] != '\0')
	return (i + 1);
    }

  return -1;
}
