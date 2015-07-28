#include <stdio.h>
#define N 10000

void quick_sort(int *data, int size, long *count);

int main(void)
{
  FILE *myFile;
  myFile = fopen("QuickSort.txt", "r");

  int data[N];
  long num = 0;
  int i;

  for (i = 0; i < N; i++)
    fscanf(myFile, "%d", &data[i]);
  printf("%d\n", data[N-1]);

  quick_sort(data, N, &num);
  printf("There are totally %ld comparisons.\n", num);
  printf("The last sorted number is %d\n", data[N-1]);

  return 0;
}

void quick_sort(int *arry, int size, long *n)
{
  int i, j, temp;
  int *first, *middle, *end;

  if (size <= 1)
    return;

  first = &arry[0];
  end = &arry[size - 1];
  if (size % 2 == 0)
    middle = &arry[size / 2 - 1];
  else
    middle = &arry[size / 2];

  if (*first <= *middle)
    {
      if (*middle <= *end)
	{
	  temp = arry[0];
	  arry[0] = *middle;
	  *middle = temp;
	}
      else if (*end <= *first)
	;
      else
	{
	  temp = arry[0];
	  arry[0] = *end;
	  *end = temp;
	}
    }
  else if (*first > *middle)
    {
      if (*end >= *first)
	;
      else if (*end <= *middle)
	{
	  temp = arry[0];
	  arry[0] = *middle;
	  *middle = temp;
	}
      else
	{
	  temp = arry[0];
	  arry[0] = *end;
	  *end = temp;
	}
    }

  for (i = j = 1; j < size; j++)
    {
      if (i == j)
	{
	  if (arry[j] <= arry[0])
	    i++;
	  else
	    ;
	}
      else
	{
	  if (arry[j] <= arry[0])
	    {
	      temp = arry[j];
	      arry[j] = arry[i];
	      arry[i++] = temp;
	    }
	  else
	    ;
	}
      (*n)++;
    }
  temp = arry[0];
  arry[0] = arry[i - 1];
  arry[i - 1] = temp;

  quick_sort(arry, i - 1, n);
  quick_sort(&(arry[i]), size - i, n);
}
