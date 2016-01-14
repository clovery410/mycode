#include <stdio.h>
#include <stdlib.h>

int search(int* nums, int numsSize, int traget) {
  int i, j, mid;
  i = 0;
  j = numsSize - 1;

  while (i < j) {
    mid = (j - i) / 2;
    if (nums[mid] == target)
      return mid;
    if (target > nums[mid]) {
      if ()
	i = mid + 1;
      
	
      j = mid - 1;
    if (
    
  
}
