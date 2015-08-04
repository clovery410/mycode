#include <stdio.h>

#define NUM_LENGTH (10)

int main()
{
  /* assume number of different word length < 10 */
  int lengths[NUM_LENGTH];
  char c;
  int length = 0;
  int max_length = 0;
  int i,j;

  for (i = 0; i < NUM_LENGTH; ++i)
    lengths[i] = 0;

  while ((c = getchar()) != EOF)
    {
      if (c != ' ')
        length++;
      else
        {
          lengths[length]++;
          length = 0;
        }
    }
  /* why */
  lengths[length]++;

  /* output result */
  for (i = 1; i < NUM_LENGTH; ++i)
    {
      putchar('0'+i);
      putchar(' ');
      for (j = 0; j < lengths[i]; ++j)
        putchar('*');
      putchar('\n');
    }

  /* output result vertical */
  for (i = 1; i < NUM_LENGTH; ++i)
    if (max_length < lengths[i])
      max_length = lengths[i];

  for (i = max_length; i >= 1; --i)
    {
    for (j = 1; j < NUM_LENGTH; ++j)
      {
        if (lengths[j] == i)
          {
            putchar('*');
            lengths[j]--;
          }
        else
          putchar(' ');
      }
    putchar('\n');
    }
  for (j = 1; j < NUM_LENGTH; ++j)
    putchar('0'+j);

  putchar('\n');
  return 0;
}

      
      
