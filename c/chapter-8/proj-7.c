#include <stdio.h>

int main(void)
{
  int i, j, matrix[5][5];
  long sum;

  for (i = 0; i < 5; i++) {
    printf("Enter row %d: ", i + 1);
    for (j = 0; j < 5; j++)
      scanf("%d", &matrix[i][j]);
  }

  printf("Row totals:");
  for (i = 0; i < 5; i++) {
    for (j = 0, sum = 0; j < 5; j++)
      sum += matrix[i][j];
    printf(" %ld", sum);
  }

  printf("\nColumn totals:");
  for (j = 0; j < 5; j++) {
    for (i = 0, sum = 0; i < 5; i++)
      sum += matrix[i][j];
    printf(" %ld", sum);
  }

  printf("\n");
  return 0;
}
