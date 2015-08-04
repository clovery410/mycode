#include <stdio.h>

int main(void)
{
  float income, tax;

  printf("Enter the amount of taxable income: ");
  scanf("%f", &income);

  if (income < 750.00f)
    tax = income * .01f;
  else if (income < 2250.00f)
    tax = 7.50f + (income - 750.00f) * .02f;
  else if (income < 3750.00f)
    tax = 37.50f + (income - 2250.00f) * .03f;
  else if (income < 5250.00f)
    tax = 82.50f + (income - 3750.00f) * .04f;
  else if (income < 7000.00f)
    tax = 142.50f + (income - 5250.00f) * .05f;
  else
    tax = 230.00f + (income - 7000.00f) * .06f;

  printf("Your tax due is: %.2f\n", tax);

  return 0;
}
