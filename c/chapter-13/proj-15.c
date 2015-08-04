#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

#define STACK_SIZE 100
#define N 100

/* external variables */
int content[STACK_SIZE];
int top = 0;

/* prototypes */
int read_line(char str[], int n);
int evaluate_RPN_expression(const char *expression);
void read_rpn(void);
void eval_rpn(char ch);
void make_empty(void);
bool is_empty(void);
bool is_full(void);
void push(int i);
int pop(void);
void stack_overflow(void);
void stack_underflow(void);

int main(void)
{
  for (;;) {
    read_rpn();
  }
  
  return 0;
}

int read_line(char str[], int n)
{
  int ch, i = 0;

  while ((ch = getchar()) != '\n')
    if (i < n)
      str[i++] = ch;
  str[i] = '\0';
  return i;
}

int evaluate_RPN_expression(const char *expression)
{
  int i;

  for (i = 0; expression[i] != '\0'; i++) {
    printf("%c\n", expression[i]);
    if (expression[i]  >= '0' && expression[i] <= '9') {
      push(expression[i] - '0');
    }
    else if (expression[i] == ' ')
      continue;
    else if (expression[i] == '=') {
      return pop();
    }
    else {
      eval_rpn(expression[i]);
    }
  }
  return pop();
}

void read_rpn(void)
{
  char rpn[N];
  int result;
  printf("Enter an RPN expression: ");
  read_line(rpn, N);
  result = evaluate_RPN_expression(rpn);
  printf("Value of expression: %d\n", result);
  //printf("Enter an RPN expression: ");
  /* while (!is_full()) { */
  /*   scanf(" %c", &ch); */
  /*   if (ch >= '0' && ch <= '9') { */
  /*     push(ch - '0'); */
  /*   } */
  /*   else { */
  /*     eval_rpn(ch); */
  /*   } */
  /* } */
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
  /* case '=':  */
  /*   printf("Value of expression: %d\n", pop()); */
  /*   printf("Enter an RPN expression: "); */
  /*   break; */
  default:
    exit(EXIT_SUCCESS);
  }
} 

void make_empty(void)
{
  top = 0;
}

bool is_empty(void)
{
  return top == 0;
}

bool is_full(void)
{
  return top == STACK_SIZE;
}

void push(int i)
{
  if (is_full()) {
    stack_overflow();
  }
  else {
    content[top++] = i;
  }
}

int pop(void)
{
  if (is_empty()) {
    stack_underflow();
  }
  else {
    return content[--top];
  }

  return 0; /* get rid of compiler warning */
} 

void stack_overflow(void)
{
  printf("Expression is too complex\n");
  exit(EXIT_SUCCESS);
}

void stack_underflow(void)
{
  printf("Not enough operands in expression\n");
  exit(EXIT_SUCCESS);
}
