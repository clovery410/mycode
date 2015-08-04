#include <stdio.h>

int main(void)
{
  char operator;
  int num1, denom1, num2, denom2;

  printf("Enter two fractions separated by an operator sign: ");
  scanf("%d/%d %c %d/%d", &num1, &denom1, &operator, &num2, &denom2);

  switch (operator) {
  case '+':
    printf("The sum is %d/%d\n", num1 * denom2 + num2 * denom1, denom1 * denom2);
    break;
  case '-':
    printf("The difference is %d/%d\n", num1 * denom2 - num2 * denom1, denom1 * denom2);
    break;
  case '*':
    printf("The product is %d/%d\n", num1 * num2, denom1 * denom2);
    break;
  case '/': 
    printf("The quotient is %d/%d\n", num1 * denom2, denom1 * num2);
    break;
  default:
    break;
  }

  return 0;
}
