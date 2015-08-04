#include <stdio.h>

#define NUM_RATES ((int) (sizeof(value) / sizeof(value[0])))
#define INITIAL_BALANCE 100.0

int main(void)
{
  int i, low_rate, month, num_year, year;
  double value[5];

  printf("Enter interest rate: ");
  scanf("%d", &low_rate);
  printf("Enter number of year: ");
  scanf("%d", &num_year);

  printf("\nYears");
  for (i = 0; i < NUM_RATES; i++) {
    printf("%6d%%", low_rate + i);
    value[i] = INITIAL_BALANCE;
  }
  printf("\n");

  for (year = 1; year <= num_year; year++) {
    printf("%3d    ", year);
    for (i = 0; i < NUM_RATES; i++) {
      for (month = 1; month <= 12; month++)
	value[i] += (double) (low_rate + i) / 12 / 100.0 * value[i];
      printf("%7.2lf", value[i]);
    }
    printf("\n");
  }

  return 0;
}
