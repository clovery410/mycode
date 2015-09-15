#include <stdio.h>
#include <limits.h>

int reverse(int x) {
  long rev_num = 0;

  if (x > INT_MAX || x < INT_MIN)
    return 0;
  
  else if ((x / 10) == 0) {
    return x;
  }

  printf("x vlaue is: %d\n", x);
  while (x != 0) {
    rev_num = rev_num * 10;
    rev_num += x % 10;
    if (rev_num > INT_MAX || rev_num < INT_MIN)
      return 0;
    x = x / 10;
  }
  return (int)rev_num;
}

int main(void) {
  int num, result;
  num = 1534236469;
  result = reverse(num);

  printf("%d\n", result);

  return 0;
}
