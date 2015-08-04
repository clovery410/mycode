#include <stdio.h>
#include <stdbool.h>

#define N 5
bool has_zero(int a[], int n);

int main(void)
{
  int i, a[N];
  
  printf("Enter %d numbers: ", N);
  for (i = 0; i < N; i++)
    scanf("%d", &a[i]);

  if (has_zero(a, N))
    printf("True\n");

  else
    printf("False\n");

  return 0;
}

bool has_zero(int a[], int n)
{
  int i;

  for (i = 0; i < n; i++)
    if (a[i] == 0)
      return true;
  
  return false;
}
