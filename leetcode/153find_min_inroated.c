#include <stdio.h>
#include <stdlib.h>

int findMin(int* nums, int numsSize) {
  int i, j;

  if (numsSize < 1)
    return 0;
  else if (numsSize == 1)
    return nums[0];

  else {
    for (i = 0; i < numsSize - 1; i++) {
      j = i + 1;
      if (nums[j] < nums[i]) {
	break;
      }
    }
    
    if (nums[0] < nums[j])
      return nums[0];
    else
      return nums[j];
  }
}

int findMinBinary(int* nums, int numsSize) {
  int mid;
  mid = numsSize / 2;
  
  if (numsSize == 0)
    return 0;
  if (numsSize == 1 || nums[0] < nums[numsSize - 1])
    return nums[0];
  
  if (numsSize <= 2) {
    if (nums[0] > nums[1])
      return nums[1];
    else
      return nums[0];
  }
  
  if (nums[0] > nums[mid])
    return findMinBinary(nums, mid + 1);
  else
    return findMinBinary(nums + mid, numsSize - mid);
  
}
int main(void) {
  int nums[7] = {1, 2, 3, 4, 5, 6, 7};
  int result;

  result = findMinBinary(nums, 7);
  printf("Minimum number is %d\n", result);

  return 0;
}
