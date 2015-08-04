#include <stdio.h>
#include <stdbool.h>

#define NUM_ROWS 7
#define NUM_COLS 24
int temperatures[NUM_ROWS][NUM_COLS] = {{2, 3, 4},
					{1, 8, 9, 10},
					{33, 20, 40, 12, 60},
					{1, 1, 1, 1, 1, 1, 1, 1},
					{0, 2, 3, 4, 5, 6, 7, 8, 9, 10},
					{5, 15, 25, 15, 25, 15, 25, 15, 35},
					{10, 20, 30, 40, 50, 40, 30}};

int find_largest(int *a, int n);

int main(void)
{
  int i, largest, temp;

  largest = temperatures[0][0];
  for (i = 0; i < NUM_ROWS; i++) {
    temp = find_largest(temperatures[i], NUM_COLS);
    if (temp > largest) {
      largest = temp;
    }
  }

  printf("Highest tamp is %d\n", largest);
  return 0;
}

int find_largest(int *a, int n)
{
  int i, max;

  max = *a;
  for (i = 0; i < n; i++) {
    if (*(a + i) > max) {
      max = *(a + i);
    }
  }
  return max;
}
