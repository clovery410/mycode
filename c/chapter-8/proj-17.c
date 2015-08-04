#include <stdio.h>

#define NUM 99
int main(void)
{
  int i, j, size, n, magic_square[NUM][NUM], row_sum, col_sum, dia_sum, dia_sum2;

  //  magic_square[N][N] = {0};
  
  printf("This program creates a magic square of a specified size.\n");
  printf("The size must be an odd number between 1 and %d.\n", NUM);
  printf("Enter size of magic square: ");
  scanf("%d", &size);

  for (i = 0; i < size; i++) {
    for (j = 0; j < size; j++)
      magic_square[i][j] = 0;
  }

  for (i = 0, j = size / 2, n = 1; n <= size * size; n++) {
    if (magic_square[i][j]) {
      i = (i + 2) % size;
      j = (j - 1 + size) % size;
    }
    magic_square[i][j] = n;
    i = (i - 1 + size) % size;
    j = (j + 1) % size;
  }

  for (i = 0; i < size; i++) {
    for (j = 0; j < size; j++) 
      printf("%5d", magic_square[i][j]);
    printf("\n");
  }

  /*************************************
   ***  Below codes are for testing  ***
   ************************************/
  for (i = 0; i < size; i++) {
    for (j = 0, row_sum = 0; j < size; j++)
      row_sum += magic_square[i][j];
    printf("Sum of row %d is %d\n", i, row_sum);
  }

  for (j = 0; j < size; j++) {
    for (i = 0, col_sum = 0; i < size; i++)
      col_sum += magic_square[i][j];
    printf("Sum of column %d is %d\n", j, col_sum);
  }

  for (i = 0, j = 0, dia_sum = 0; i < size; i++, j++)
    dia_sum += magic_square[i][j];
  printf("Diagonal sum is %d\n", dia_sum);

  for (i = 0, j = size - 1, dia_sum2 = 0; i < size; i++, j--)
    dia_sum2 += magic_square[i][j];
  printf("Opposite diagonal sum is %d\n", dia_sum2);

  return 0;
}
