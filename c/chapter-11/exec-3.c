#include <stdio.h>

#define N 10

void avg_sum(double a[], int n, double *avg, double *sum);

int main(void)
{
  double b[N], num_avg, num_sum;
  int i;

  printf("Enter %d numbers: ", N);
  for (i = 0; i < N; i++) {
    scanf("%lf", &b[i]);
  }

  avg_sum(b, N, &num_avg, &num_sum);

  printf("Average of the array is: %lf\n", num_avg);
  printf("Sum of the array is: %lf\n", num_sum);

  return 0;
}

void avg_sum(double a[], int n, double *avg, double *sum)
{
  int i;

  *sum = 0.0;
  for (i = 0; i < n; i++) {
    *sum += a[i];
    *avg = *sum / n;
  }
}
