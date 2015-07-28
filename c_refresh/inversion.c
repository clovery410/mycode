#include <stdio.h>
#include <stdlib.h>
#define N 100000

void count (int arry[], int n, long *total);
void count_split (int left[], int right[], int size, long *total);

int main (void)
{
  FILE *myFile;
  myFile = fopen("IntegerArray.txt", "r");
  int data[N];
  int i;
  //  int *num = malloc(sizeof(int));
  long num = 0;

  for (i = 0; i < N; i++)
    fscanf(myFile, "%d", &data[i]);
  printf("%d\n", data[N-1]);

  count(data, N, &num);
  printf("There are total %ld inversions.\n", num);
  printf("%d\n", data[N-1]);
  /*  for (i = 0; i < N; i++)
    printf("%d ", data[i]);
  */
  return 0;
}

void count (int arry[], int n, long *total)
{ 
  if (n == 1)
    return;
  else
    {
      count(arry, n / 2, total);
      count(&(arry[n / 2]), n - n / 2, total);

      count_split(arry, &(arry[n / 2]), n, total);
    }
}

void count_split (int left[], int right[], int size, long *total)
{
  int i, j, k;
  int *a = malloc(size / 2 * sizeof(int));
  int *b = malloc((size - size / 2) * sizeof(int));

  /*  printf("data: ");
  for (i = 0; i < size; ++i) {
    printf("%d ", left[i]);
  }
  printf("\n");
  */
  for (i = 0; i < size / 2; i++)
    a[i] = left[i];
  for (j = 0; j < size - size / 2; j++)
    b[j] = right[j];

  for (i = j = k = 0; k < size; k++)
    {
      if (i >= size / 2)
	{
	  left[k] = b[j++];
	  *total += (size / 2 - i);
	  //	  printf("Left %d\n", *total);
	}
      else if (j >= size - size / 2)
	left[k] = a[i++];
      else if (a[i] <= b[j])
	left[k] = a[i++];
      else
	{
	  left[k] = b[j++];
	  *total += (size / 2 - i);
	  //	  printf("Split %d\n", *total);
	}
    }

}
