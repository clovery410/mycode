#include <stdio.h>

void pay_amount(int dollars, int *twenties, int *tens, int *fives, int *ones);

int main(void)
{
  int amount, twenty_dollar, ten_dollar, five_dollar, one_dollar;

  printf("Enter a dollar amount: ");
  scanf("%d", &amount);

  pay_amount(amount, &twenty_dollar, &ten_dollar, &five_dollar, &one_dollar);

  printf("$20 bills: %d\n", twenty_dollar);
  printf("$10 bills: %d\n", ten_dollar);
  printf(" $5 bills: %d\n", five_dollar);
  printf(" $1 bills: %d\n", one_dollar);

  return 0;
}

void pay_amount(int dollars, int *twenties, int *tens, int *fives, int *ones)
{
  *twenties = dollars / 20;
  *tens = (dollars - *twenties * 20) / 10;
  *fives = (dollars - *twenties * 20 - *tens * 10) / 5;
  *ones = dollars - *twenties * 20 - *tens * 10 - *fives * 5;
}
