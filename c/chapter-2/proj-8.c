#include <stdio.h>

int main(void)
{
  float loan_amount, bank_rate, monthly_payment, remaining_after_first, remaining_after_second, remaining_after_third;

  printf("Enter amount of loan: ");
  scanf("%f", &loan_amount);
  printf("Enter interest rate: ");
  scanf("%f", &bank_rate);
  printf("Enter monthly payment: ");
  scanf("%f", &monthly_payment);

  remaining_after_first = loan_amount - monthly_payment + loan_amount * bank_rate / 100.0f / 12.0f;
  remaining_after_second = remaining_after_first - monthly_payment + remaining_after_first * bank_rate / 100.0f / 12.0f;
  remaining_after_third = remaining_after_second - monthly_payment + remaining_after_second * bank_rate / 100.0f / 12.0f;

  printf("Balance remaining after first payment: $%.2f\n", remaining_after_first);
  printf("Balance remaining after second payment: $%.2f\n", remaining_after_second);
  printf("Balance remaining after third payment: $%.2f\n", remaining_after_third);

  return 0;
}
