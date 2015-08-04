#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

#define STACK_SIZE 100

int contents[STACK_SIZE];
int *top_ptr;

void make_empty(void);
bool is_empty(void);
bool is_full(void);
void push(int i);
int pop(void);
void stack_overflow(void);
void stack_underflow(void);

int main(void)
{
  int i, j;
  make_empty();
  printf("Enter: ");
  scanf("%d", &i);
  push(i);
  push(i);
  //push(i);
  
  if (is_empty())
    printf("It is empty now\n");
  else {
    printf("It is not empty\n");
    printf("Top is %d\n", pop());
  }
  return 0;
}

void make_empty(void)
{
  top_ptr = contents;
}

bool is_empty(void)
{
  return top_ptr == contents;
}

bool is_full(void)
{
  return top_ptr == contents + STACK_SIZE;
}

void push(int i)
{
  if (is_full())
    stack_overflow();
  else
    *top_ptr++ = i;
}

int pop(void)
{
  if (is_empty())
    stack_underflow();
  else
    return *--top_ptr;

  return 0;
}

void stack_overflow(void)
{
  printf("Stack overflow\n");
  exit(EXIT_SUCCESS);
}

void stack_underflow(void)
{
  printf("Stack underflow\n");
  exit(EXIT_SUCCESS);
}
