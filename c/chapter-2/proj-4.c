#include <stdio.h>

int main(void)
{
  float tax_rate, price, total;
  tax_rate = 0.05f;
  
  printf("Enter an amount: ");
  scanf("%f", &price);

  total = price * (1.0f + tax_rate);
  
  printf("With tax added: $%.2f\n", total);

  return 0;
}
