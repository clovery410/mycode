#include <stdio.h>

int main(void)
{
  float operand, result;
  char operator;

  printf("Enter an expression: ");
  
  scanf("%f", &result);

  while ((operator = getchar()) != '\n') {
    scanf("%f", &operand);
    switch (operator) {
    case '+': result += operand; break;
    case '-': result -= operand; break;
    case '*': result *= operand; break;
    case '/': result /= operand; break;
    default: break;
    }
  }
  printf("Value of expression: %g\n", result);

  return 0;
}
    
