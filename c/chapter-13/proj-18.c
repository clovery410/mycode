#include <stdio.h>

int main(void)
{
  int month, day, year;
  char *str[] = {"January", "February", "March", "April", "May", "June",
		 "July", "August", "September", "October", "Novenber", "December"};

  printf("Enter a date (mm/dd/yyyy): ");
  scanf("%d/%d/%d", &month, &day, &year);

  printf("You entered the date %s %d, %d\n", str[month - 1], day, year);

  return 0;
}
