#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <time.h>

#define R 10
#define C 10
#define CH_START 'A'
#define CH_END 'Z'

void generate_random_walk(char walk[R][C]);
void print_array(char walk[R][C]);

int main(void)
{
  char walk[R][C];

  generate_random_walk(walk);

  print_array(walk);

  return 0;
}

void generate_random_walk(char walk[R][C])
{
  int i, j, x = 0, y = 0, n, d = 0;
  int direction[4] = {-1, 1, 1, -1};
  char ch;
  
  for (i = 0; i < R; i++) {
    for (j = 0; j < C; j++)
      walk[i][j] = '.';
  }

  srand((unsigned) time (NULL));

  walk[x][y] = CH_START;
  for (ch = CH_START + 1; ch <= CH_END; ch++) {
    n = rand() % 4;
    for (i = 0; i < 4; i++) {
      printf("%d ", n);
      d = direction[n];
      if (n % 2 == 0 && ((x + d) < 0 || (x + d) >= R))
        n = (n + 1) % 4;
      else if (n % 2 == 1 && ((y + d) < 0 || (y + d) >= C))
        n = (n + 1) % 4;
      else if (n % 2 == 0 && walk[x+d][y] != '.')
        n = (n + 1) % 4;
      else if (n % 2 == 1 && walk[x][y+d] != '.')
        n = (n + 1) % 4;
      else {
        printf("-- print %c\n", ch);
        break;
      }
    }
    if (i >= 4) {
      printf("-- Game Over\n");
      break;
    }
    else if (n % 2 == 0)
      x += d;
    else if (n % 2 == 1)
      y += d;

    walk[x][y] = ch;
  }
}

void print_array(char walk[R][C])
{
  int i, j;

  printf("\nHere comes the maze:\n");
  for (i = 0; i < R; i++) {
    for (j = 0; j < C; j++)
      printf("%c ", walk[i][j]);
    printf("\n");
  }
}
