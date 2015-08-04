#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include "stack.h"

void read_rpn(void);
void eval_rpn(char ch);

int main(void)
{
  for (;;) {
    read_rpn();
  }
  
  return 0;
}

void read_rpn(void)
{
  char ch;
  printf("Enter an RPN expression: ");
  while (!is_full()) {
    scanf(" %c", &ch);
    if (ch >= '0' && ch <= '9') {
      push(ch - '0');
    }
    else {
      eval_rpn(ch);
    }
  }
}

void eval_rpn(char ch)
{
  int operand1, operand2;

  switch (ch) {
  case '+': 
    operand2 = pop();
    operand1 = pop();
    push(operand1 + operand2);
    break;
  case '-': 
    operand2 = pop();
    operand1 = pop();
    push(operand1 - operand2);
    break;
  case '*': 
    operand2 = pop();
    operand1 = pop();
    push(operand1 * operand2);
    break;
  case '/': 
    operand2 = pop();
    operand1 = pop();
    push(operand1 / operand2);
    break;
  case '=': 
    printf("Value of expression: %d\n", pop());
    printf("Enter an RPN expression: ");
    break;
  default:
    exit(EXIT_SUCCESS);
  }
}
