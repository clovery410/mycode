#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

bool leap_year;
int num_days[12] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

void split_date(int day_of_year, int year, int *month, int *day);

int main(void)
{
  int day_of_year, year, month, day;

  printf("Enter year: ");
  scanf("%d", &year);
  printf("Enter the day of year (between 1 and 366): ");
  scanf("%d", &day_of_year);

  split_date(day_of_year, year, &month, &day);

  printf("This specific date is %.2d/%.2d/%d\n", month, day, year);

  return 0;
}

void split_date(int day_of_year, int year, int *month, int *day)
{
  int i;
  *month = 1;
  
  /* Determine if year is leap year */
  if (year % 4 == 0 && (year % 100 != 0 || year % 400 == 0)) {
    leap_year = true;
  }
  else {
    leap_year = false;
  }

  if (leap_year) {
    num_days[1] = 29;
  }

  if (!leap_year && day_of_year == 366) {
    printf("Comment year only has 365 days!\n");
    exit(EXIT_SUCCESS);
  }
  
  for (i = 0; i < 12 && day_of_year > num_days[i]; i++) {
    day_of_year -= num_days[i];
    *month += 1;
  }
  *day = day_of_year;
}
