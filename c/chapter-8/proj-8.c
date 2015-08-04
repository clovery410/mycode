#include <stdio.h>

int main(void)
{
  int i, j, total, high, low, score[5][5];
  

  for (i = 0; i < 5; i++) {
    printf("Enter five quiz grades of student %d: ", i + 1);
    for (j = 0; j < 5; j++)
      scanf("%d", &score[i][j]);
  }

  printf("\nTotal score:");
  for (i = 0; i < 5; i++) {
    for (j = 0, total = 0; j < 5; j++)
      total += score[i][j];
    printf(" %d", total);
  }
  
  printf("\nAverage score:");
  for (i = 0; i < 5; i++) {
    for (j = 0, total = 0; j < 5; j++)
      total += score[i][j];
    printf(" %.1f", total / 5.0);
  }

  printf("\nAverage score for each quiz:");
  for (j = 0; j < 5; j++) {
    for (i = 0, total = 0; i < 5; i++)
      total += score[i][j];
    printf(" %.1f", total / 5.0);
  }

  printf("\nHighest score for each quiz:");
  for (j = 0; j < 5; j++) {
    for (i = 1, high = score[0][j]; i < 5; i++) {
      if (score[i][j] > high)
	high = score[i][j];
    }
    printf(" %d", high);
  }

  printf("\nLowest score for each quiz:");
  for (j = 0; j < 5; j++) {
    for (i = 1, low = score[0][j]; i < 5; i++) {
      if (score[i][j] < low)
	low = score[i][j];
    }
    printf(" %d", low);
  }

  printf("\n");
  return 0;
}
