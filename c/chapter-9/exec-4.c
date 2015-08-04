#include <stdio.h>

int day_of_year(int month, int day, int year);

int main(void)
{
  int month, day, year;

  printf("Enter the date(use the form of mm/dd/yyyy): ");
  scanf("%d/%d/%d", &month, &day, &year);

  printf("This is the %d day of year %d\n", day_of_year(month, day, year), year);

  return 0;
}

int day_of_year(int month, int day, int year)
{
  int leap_year[12] = {31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
  int common_year[12] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

  if (year % 4 == 0 && (year % 100 != 0 || year % 400 == 0)) {
    if (month == 0)
      return 0;
    else 
      return day + day_of_year(month - 1, leap_year[month - 2], year);
  }
  else {
    if (month == 0)
      return 0;
    else 
      return day + day_of_year(month - 1, common_year[month - 2], year);
  }
}

//Another version of day_of_year function
int day_of_year1(int month, int day, int year)
{
  int i, day_count = 0;
  int num_days[12] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

  for (i = 1; i < month; i++)
    day_count += num_days[i - 1];
  
  if (year % 4 == 0 && (year % 100 != 0 || year % 400 == 0))
    day_count++;

  return day + day_count;
}
