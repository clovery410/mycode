#include <stdio.h>

int main(void)
{
  int n, day, i, j;

  printf("Enter number of days in month: ");
  scanf("%d", &n);
  printf("Enter starting day of the week (1=Sun, 7=Sat): ");
  scanf("%d", &day);

  for (j = day; j > 1; j--)
    printf("   ");

  for (i = 1; i <= n; i++) {
    printf("%3d", i);
    if ((i + day - 1) % 7 == 0)
      printf("\n");
  }

  printf("\n");
  return 0;
}
