#include <stdio.h>

int main(void)
{
  float total, remainder, rate, payment;
  int num, i;

  printf("Enter amount of loan: ");
  scanf("%f", &total);
  printf("Enter interest rate: ");
  scanf("%f", &rate);
  printf("Enter monthly payment: ");
  scanf("%f", &payment);
  printf("Enter number of payments: ");
  scanf("%d", &num);

  for (i = 1, remainder = total; i <= num; i++) {
    remainder = remainder - payment + remainder * rate / 100.00f / 12.00f;
    printf("Balance remaining after %d payment: $%.2f\n", i, remainder);
  }

  return 0;
}
