#include <stdio.h>

#define N 10

double ident[N][N], *p;
int num_zeros = N;

void make_unit_matrix(void);
void print_matrix(void);

int main(void)
{
  make_unit_matrix();
  print_matrix();

  return 0;
}

void make_unit_matrix(void)
{
  for (p = &ident[0][0]; p <= &ident[N-1][N-1]; p++) {
    if (num_zeros == N) {
      *p = 1.0;
      num_zeros = 0;
    }
    else {
      *p = 0.0;
      num_zeros++;
    }
  }
}

void print_matrix(void)
{
  int i;
  double (*q)[N];
  for (q = &ident[0]; q < &ident[N]; q++) {
    for (i = 0; i < N; i++) {
      printf("%lf ", (*q)[i]);
    }
    printf("\n");
  }
  /* int i = 0; */
  /* printf("Value of int: %d\n", i + 1); */

  /* int array_1[] = {1,2,3}; */

  /* int array[][3] = {1,2,3,4,5,6,7,8,9}; */
  /* int (*p)[3] = &(array[0]); */
  /* printf("Value of (*p)[1]:%d\n", (*p)[1]);    */
  /* printf("Value of *p[1]:%d\n", *p[1]);   */
  /* printf("Value of array + 1:%d\n", array + 1);   */
  /* printf("Value of array[0]:%d\n", array[0]);   */
}
