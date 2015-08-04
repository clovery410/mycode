#include <stdio.h>

#define N 5

double inner_product(double a[], double b[], int n);

int main(void)
{
  int i;
  double a[N], b[N];

  printf("Enter elements of array a: ");
  for (i = 0; i < N; i++)
    scanf("%lf", &a[i]);

  printf("Enter elements of array b: ");
  for (i = 0; i < N; i++)
    scanf("%lf", &b[i]);

  printf("The result of inner product is %lf\n", inner_product(a, b, N));

  return 0;
}

double inner_product(double a[], double b[], int n)
{
  int i;
  double sum = 0.0;

  for (i = 0; i < n; i++)
    sum += a[i] * b[i];

  return sum;
}
