#include <stdio.h>
#define N 10000

void quick_sort(int *data, int size, long *count);

int main(void)
{
  FILE *myFile;
  myFile = fopen("QuickSort.txt", "r");

  int data[N];
  int i;
  long num = 0;

  for (i = 0; i < N; i++)
    fscanf(myFile, "%d", &data[i]);
  printf("%d\n", data[N-1]);

  quick_sort(data, N, &num);
  printf("There are total %ld comparisons.\n", num);
  printf("The last sorted number is %d\n", data[N-1]);

  return 0;
}

void quick_sort(int *arry, int size, long *n)
{
  int i, j, temp;

  if (size <= 1)
    return;

  else
    {
      temp = arry[0];
      arry[0] = arry[size - 1];
      arry[size - 1] = temp;
      
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
      
    }
  
  temp = arry[0];
  arry[0] = arry[i - 1];
  arry[i - 1] = temp;
   

  quick_sort(arry, i - 1, n);
  quick_sort(&(arry[i]), size - i, n);
}
