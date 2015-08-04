#include <stdio.h>

#define NUM 99

void create_magic_square(int n, char magic_square[n][n]);
void print_magic_square(int n, char magic_square[n][n]);

int main(void)
{
  int n;
    
  printf("This program creates a magic square of a specified size.\n");
  printf("The size must be an odd number between 1 and %d.\n", NUM);
  printf("Enter size of magic square: ");
  scanf("%d", &n);

  char magic_square[n][n];

  create_magic_square(n, magic_square);
  print_magic_square(n, magic_square);

  return 0;
}

void create_magic_square(int n, char magic_square[n][n])
{
  int i, j, num;

  for (i = 0; i < n; i++)
    for (j = 0; j < n; j++)
      magic_square[i][j] = 0;

  for (i = 0, j = n / 2, num = 1; num <= n * n; num++) {
    if (magic_square[i][j]) {
      i = (i + 2) % n;
      j = (j - 1 + n) % n;
    }
    magic_square[i][j] = num;
    i = (i - 1 + n) % n;
    j = (j + 1) % n;
  }
}

void print_magic_square(int n, char magic_square[n][n])
{
  int i, j;

  for (i = 0; i < n; i++) {
    for (j = 0; j < n; j++)
      printf("%5d", magic_square[i][j]);
    printf("\n");
  }
}
