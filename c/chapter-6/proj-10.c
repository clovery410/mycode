#include <stdio.h>

int main(void)
{
  int day, month, year, target_day, target_month, target_year;

  printf("Enter a date (mm/dd/yy): ");
  scanf("%d/%d/%d", &month, &day, &year);

  for (target_day = day, target_month = month, target_year = year; ;) {
    printf("Enter a date (mm/dd/yy): ");
    scanf("%d/%d/%d", &month, &day, &year);
    if (year == 0 && month == 0 && day == 0)
      break;
    else if (year > target_year)
      continue;
    else if (year == target_year && month > target_month)
      continue;
    else if (year == target_year && month == target_month && day >= target_day)
      continue;
    else {
      target_year = year;
      target_month = month;
      target_day = day;
    }
  }
  
  printf("%d/%d/%.2d is the earliest date\n", target_month, target_day, target_year);

  return 0;
}
