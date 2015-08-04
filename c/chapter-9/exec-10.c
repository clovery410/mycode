#include <stdio.h>

int largest(int a[], int n);
int average(int a[], int n);
int num_positive(int a[], int n);

int main(void)
{
  int n, i;

  printf("Enter length of the array: ");
  scanf("%d", &n);

  int a[n];

  printf("Ente array elements: ");
  for (i = 0; i < n; i++)
    scanf("%d", &a[i]);
  
  printf("The largest element of this array is: %d\n", largest(a, n));
  printf("The average of all elements in this array is: %d\n", average(a, n));
  printf("The number of positive elements in this array is: %d\n", num_positive(a, n));

  return 0;
}

int largest(int a[], int n)
{
  int i, max = a[0];

  for (i = 1; i < n; i++)
    if (a[i] > max)
      max = a[i];

  return max;
}

int average(int a[], int n)
{
  int i, sum = 0;

  for (i = 0; i < n; i++)
    sum += a[i];

  return sum / n;
}

int num_positive(int a[], int n)
{
  int i, count = 0;

  for (i = 0; i < n; i++)
    if (a[i] > 0)
      count++;

  return count;
}
