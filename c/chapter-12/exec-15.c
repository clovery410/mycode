#include <stdio.h>
#include <stdbool.h>

#define NUM_ROWS 7
#define NUM_COLS 24
int temperatures[NUM_ROWS][NUM_COLS] = {{2, 3, 4},
					{1, 8, 9, 10},
					{33, 20, 40, 12},
					{1, 1, 1, 1, 1, 1, 1, 1},
					{0, 2, 3, 4, 5, 6, 7, 8, 9, 10},
					{5, 15, 25, 15, 25, 15, 25, 15, 35},
					{10, 20, 30, 40, 50, 60, 70}};

int main(void)
{
  int i, *p;

  printf("Enter which day: ");
  scanf("%d", &i);
  for (p = temperatures[i]; p < temperatures[i] + NUM_COLS; p++) {
    //  for (p = temperatures[i]; p < temperatures[i + 1]; p++) {  
    printf("p[i]: %d", *p);
  }

  return 0;
}
