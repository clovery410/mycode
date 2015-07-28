#include <stdio.h>

void squeeze (char s1[], char s2[]);

int main (void)
{
  char first[] = "3234562";
  char second[] = "239";

  squeeze(first, second);
  printf("The squeezed string is: %s\n", first);

  return 0;
}

void squeeze (char s1[], char s2[])
{
  int i, j, k;

  for (i = k = 0; s1[i] != '\0'; i++)
    {
      for (j = 0; (s2[j] != '\0') && (s1[i] != s2[j]); j++)
	;
      if (s2[j] == '\0')
	s1[k++] = s1[i];
      else
	s1[k] = s1[i+1];
    }
  
  s1[k] = '\0';
}
