#include <stdio.h>
#include <stdlib.h>

int max(int a, int b) {
  if (a > b)
    return a;
  else
    return b;
     
}
int rob(int* nums, int numsSize) {
  int i, A[numsSize];

  printf("n is: %d\n", numsSize);
  /* for (i = 2; i < numsSize; i++) */
  /*   A[i] = 0; */

  A[0] = nums[0];
  A[1] = max(nums[0], nums[1]);
  printf("A[0] is: %d, A[1] is: %d\n", A[0], A[1]);
  for (i = 2; i < numsSize; i++) {
    printf("check value %d\n", nums[i]);
    A[i] = max(A[i - 1], A[i - 2] + nums[i]);
  }

  return A[numsSize - 1];
}

int main(void) {
  int array[] = {1, 2, 7, 4};
  int n = 4;
  int result;

  result = rob(array, n);
  printf("%d\n", result);

  return 0;
}
