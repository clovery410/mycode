#include <stdio.h>

int main(void)
{
  int amount, twenty_dollar, ten_dollar, five_dollar, one_dollar;
  
  printf("Enter a dollar amount: ");
  scanf("%d", &amount);

  twenty_dollar = amount / 20;
  ten_dollar = (amount - twenty_dollar * 20) / 10;
  five_dollar = (amount - twenty_dollar * 20 - ten_dollar * 10) / 5;
  one_dollar = amount - twenty_dollar * 20 - ten_dollar * 10 - five_dollar * 5;

  printf("$20 bills: %d\n", twenty_dollar);
  printf("$10 bills: %d\n", ten_dollar);
  printf(" $5 bills: %d\n", five_dollar);
  printf(" $1 bills: %d\n", one_dollar);

  return 0;
}
