#include <stdio.h>

#define N 10

int b[N] = {101, 23, 45, 64, 3, 70, 99, 38, 50, 21};

void find_two_largest(const int *a, int n, int *largest, int *second_largest);

int main(void)
{
  //int size_t = sizeof(a) / sizeof(a[0]);
  int first, second;

  find_two_largest(b, N, &first, &second);

  printf("Largest value is: %d\n", first);
  printf("Second largest is: %d\n", second);

  return 0;
}

void find_two_largest(const int *a, int n, int *largest, int *second_largest)
{
  int i;
  
  if (*(a + 1) > *a) {
    *largest = *(a + 1);
    *second_largest = *a;
  }
  else {
    *largest = *a;
    *second_largest = *(a + 1);
  }

  for (i = 2; i < n; i++) {
    if (*(a + i) > *largest) {
      *second_largest = *largest;
      *largest = *(a + i);
    }
    else if (*(a + i) > *second_largest) {
      *second_largest = *(a + i);
    }
  }
}
  
