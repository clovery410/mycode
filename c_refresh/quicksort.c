#include <stdio.h>
#include <stdlib.h>
#define N 10
void quick_sort(int *lst, int size);

int main (void)
{
  int data[N] = {7, 9, 4, 1, 2, 3, 8, 5, 6, 11};
  int i;

  quick_sort(data, N);
  for (i = 0; i < N; i++)
    printf("%d ", data[i]);
  printf("\n");
  
  return 0;
}

void quick_sort(int *lst, int size)
{
    int i, j, temp;
    int num;

    for (i = 0; i < size; i++)
      printf("%d ", lst[i]);
    printf("\n");
    if (size <= 1)
      return;

    else
    {
      //      int i, j, temp;
      num = rand() % size;
      if (num != 0)
	{
	  temp = lst[0];
	  lst[0] = lst[num];
	  lst[num] = temp;
      	  printf("Pivot is %d\n", lst[0]);
	}

      for (i = j = 1; j < size; j++)
	{
	  if (i == j)
	    {
	      if (lst[j] <= lst[0])
		i++;
	      else
		;
	    }
	  else
	    {
	      if (lst[j] <= lst[0])
		{
		  temp = lst[j];
		  lst[j] = lst[i];
		  lst[i++] = temp;
		}
	      else
		;
	    }
    	}
      temp = lst[0];
      lst[0] = lst[i - 1];
      lst[i - 1] = temp;
      printf("Changed pivot %d and first small %d\n", lst[i - 1], lst[0]);
      //    quick_sort(lst, i - 1);
      //   quick_sort(&(lst[i]), j - i + 1);
    }
    quick_sort(lst, i - 1);
    quick_sort(&(lst[i]), j - i);
  
}
