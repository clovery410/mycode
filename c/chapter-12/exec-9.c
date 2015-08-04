#include <stdio.h>

double arr1[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
double arr2[] = {2, 2, 2, 2, 2, 2, 2, 2, 2, 2};

double inner_product(const double *a, const double *b, int n);

int main(void)
{
  int size_t = sizeof(arr1) / sizeof(arr1[0]);
  double sum_product;
				  
  sum_product = inner_product(arr1, arr2, size_t);

  printf("Inner product sum is: %lf\n", sum_product);

  return 0;
}
				  
double inner_product(const double *a, const double *b, int n)
{
  /*  double sum, *p, *q;*/
  int i;

  double sum = 0.0;
  for (i = 0; i < n; ++i) {
    sum += (*(a + i)) * (*(b + i));
  }
  
  /* for (p = a, q = b; p < a + n; p++, q++) { */
  /*   sum += (*p) * (*q); */
  /* } */

  return sum;
}
