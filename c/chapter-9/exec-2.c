#include <stdio.h>

int check(int x, int y, int n);

int main(void)
{
  int x, y, n;

  printf("Enter three numbers: ");
  scanf("%d%d%d", &x, &y, &n);

  printf("%d\n", check(x, y, n));

  return 0;
}

int check(int x, int y, int n)
{
  return (x >= 0 && x <= n - 1 && y >= 0 && y <= n - 1);
}
