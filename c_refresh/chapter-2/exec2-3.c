#include <stdio.h>

int htoi(char s[]);

int main (void)
{
  char s[] = "-0xB2";
  printf("String = %s integer = %d\n", s, htoi(s));

  return 0;
}

int htoi(char s[])
{
  int i, n, sign;

  n = 0;
  for (i = 0; s[i] == ' '; i++)
    ;
  
  if (s[i] == '-')
    sign = -1;
  else
    sign = 1;
  
  if (s[i] == '+' || s[i] == '-')
    i++;
  if (s[i] == '0' && (s[i+1] == 'x' || s[i+1] == 'X'))
    i = i + 2;

  for (; (s[i] >= '0' && s[i] <= '9') || (s[i] >= 'a' && s[i] <= 'f') || (s[i] >= 'A' && s[i] <= 'F'); ++i)
    {
      if (s[i] >= 'a' && s[i] <= 'f')
	n = n * 16 + (s[i] - 'a' + 10);
      else if (s [i] >= 'A' && s[i] <= 'F')
	n = n * 16 + (s[i] - 'A' + 10);
      else
	n = n * 16 + (s[i] - '0');
    }
  return sign * n;
}
