#include <stdio.h>
#include <stdlib.h>

#define N 1

void merge_sort (int data[], int size);
void merge (int left[], int right[], int n);

int main(void)
{
  int i;
  int lst[N] = {2};

  merge_sort(lst, N);

  for (i = 0; i < N; i++)
    printf("%d ", lst[i]);

  printf("\n");
  return 0;
}

void merge_sort(int data[], int size)
{
  if (size <= 1)
    return;

  else
    {
      merge_sort(data, size / 2);
      merge_sort(&(data[size / 2]), size - size / 2);

      merge(data, &(data[size / 2]), size);
    }
}

void merge(int left[], int right[], int size)
{
  int i, j, k;
  int* a = malloc((size / 2) * sizeof(int));
  int* b = malloc((size - size / 2) * sizeof(int));

  for (i = 0; i < size / 2; i++)
    a[i] = left[i];
  for (j = 0; j < size - size / 2; j++)
    b[j] = right[j];

  for (i = j = k = 0; k < size; k++)
    {
      if (i >= size / 2)
	left[k] = b[j++];
      else if (j >= size - size / 2)
	left[k] = a[i++];
      else if (a[i] <= b[j])
	left[k] = a[i++];
      else
	left[k] = b[j++];
    }
}
