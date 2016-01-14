#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define MAX 99999

int checkPerfect(int n) {
  int sq = sqrt(n);
  if (sq * sq == n)
    return 1;
  else
    return 0;
}

int min(int a, int b) {
  if (a <= b)
    return a;
  else
    return b;
}

int numSquares(int n) {
  int i, j, key, A[n+1];

  A[0] = 0;
  for (i = 1; i <= n; i++)
    A[i] = i;

  for (i = 2; i <= n; i++) {
    if (checkPerfect(i))
      A[i] = 1;
    else {
      key = sqrt(i);
      for (j = key; j > 1; j--) 
	A[i] = min((1 + A[i - j * j]), A[i]);
    }
  }

  return A[n];
}

int main(void) {
  int num, result;

  for (num = 1; num <= 100; num++) {
    result = numSquares(num);
    printf("%d: %d\n", num, result);
  }

  //  int result = numSquares(num);

  //  printf("result is %d\n", result);

  return 0;
}
