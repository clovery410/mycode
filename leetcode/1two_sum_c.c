#include <stdio.h>
#include <stdlib.h>

#define KEY_NOT_FOUND -1

void swap(int* a, int* b) {
  int temp;
  temp = *a;
  *a = *b;
  *b = temp;
}

int partition(int* array, int lo, int hi) {
  int pivot, i, j;
  pivot = array[lo];
  i = lo + 1;
  for (j = lo + 1; j <= hi; j++) {
    if (array[j] < pivot) {
      swap(&array[i], &array[j]);
      i++;
    }
  }
  swap(&array[lo], &array[i-1]);
  return i;
}

void quicksort(int*array, int n) {
  int p, i;
  if (n <= 1)
    return;
  p = rand() % n;
  if (p != 0)
    swap(&array[p], &array[0]);
  i = partition(array, 0, n - 1);
  quicksort(array, i - 1);
  quicksort(array + i, n - i);
}

int binarySearch(int* a, int key, int imin, int imax){
  if (imax < imin)
    return KEY_NOT_FOUND;
  else {
    int imid = (imax - imin) / 2 + imin;
    if (*(a + imid) < key)
      return binarySearch(a, key, imid+1, imax);
    else if (*(a + imid) > key)
      return binarySearch(a, key, imin, imid-1);
    else
      return imid;
  }
}

int* twoSum(int* nums, int numsSize, int target) {
  int* ret = malloc(numsSize * sizeof(int));
  int* p = malloc(2 * sizeof(int));
  int first_i, second_i, i, j;
  
  for (i = 0; i < numsSize; i++)
    ret[i] = *(nums + i);

  quicksort(nums, numsSize);
  
  for (i = 0; i < numsSize; i++) {
    second_i = binarySearch(nums, target - nums[i], 0, numsSize - 1);
    if (second_i != -1) {
      first_i = i;
      break;
    }
  }

  for (i = 0; i < numsSize; i++) {
    if (ret[i] == nums[first_i])
      break;
  }
  for (j = 0; j < numsSize; j++) {
    if (ret[j] == nums[second_i] && j != i)
      break;
  }

  if (i <= j) {
    *p = i + 1;
    *(p+1) = j + 1;
  }

  else {
    *p = j + 1;
    *(p+1) = i + 1;
  }
  return p;
}

int main(void) {
  int inputs[5] = {11, 9, 15, 7, 2};
  int n = sizeof(inputs) / sizeof(int);
  int t = 26;
  int* result;

  result = twoSum(inputs, n, t);
  printf("index1 = %d, index2 = %d\n", *result, *(result+1));
  free(result);
  return 0;
}
