#include <stdio.h>

void split_time(long total_sec, int *hr, int *min, int *sec);

int main(void)
{
  int hour, minute, second;
  long total_sec;

  printf("Enter the total second sice midnight: ");
  scanf("%ld", &total_sec);

  split_time(total_sec, &hour, &minute, &second);

  printf("The splited time is %.2d:%.2d:%.2d\n", hour, minute, second);

  return 0;
}

void split_time(long total_sec, int *hr, int *min, int *sec)
{
  *hr = total_sec / 60 / 60;
  *min = (total_sec - *hr * 3600) / 60;
  *sec = (total_sec - *hr * 3600) % 60;
}
