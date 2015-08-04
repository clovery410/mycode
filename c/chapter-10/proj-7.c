#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

#define MAX_DIGITS 10

const int segments[10][7] = {{1, 1, 1, 1, 1, 1, 0}, {0, 1, 1, 0, 0, 0, 0},
			     {1, 1, 0, 1, 1, 0, 1}, {1, 1, 1, 1, 0, 0, 1},
			     {0, 1, 1, 0, 0, 1, 1}, {1, 0, 1, 1, 0, 1, 1},
			     {1, 0, 1, 1, 1, 1, 1}, {1, 1, 1, 0, 0, 0, 0},
			     {1, 1, 1, 1, 1, 1, 1}, {1, 1, 1, 1, 0, 1, 1}};

int digits[4][MAX_DIGITS * 4];

void clear_digits_array(void);
void process_digit(int digit, int position);
void print_digits_array(void);

int main(void)
{
  char ch;
  int digit, position = 0;
  
  clear_digits_array();

  printf("Enter a number: ");
  while ((ch = getchar()) != '\n' && position < MAX_DIGITS) {
    if (ch >= '0' && ch <= '9') {
      digit = ch - '0';
      //printf("%d\n", digit);
      process_digit(digit, position);
      position++;
    }
  }
  print_digits_array();

  return 0;
}

void clear_digits_array(void)
{
  int i, j;
  for (i = 0; i < 4; i++) {
    for (j = 0; j < MAX_DIGITS * 4; j++) {
      digits[i][j] = ' ';
    }
  }
}

void process_digit(int digit, int position)
{
  int i;
  for (i = 0; i < 7; i++) {
    if (segments[digit][i]) {
      switch (i) {
      case 0: digits[0][1+position*4] = '_'; break;
      case 1: digits[1][2+position*4] = '|'; break;
      case 2: digits[2][2+position*4] = '|'; break;
      case 3: digits[2][1+position*4] = '_'; break;
      case 4: digits[2][0+position*4] = '|'; break;
      case 5: digits[1][0+position*4] = '|'; break;
      case 6: digits[1][1+position*4] = '_'; break;
      default: break;
      }
    }
  }
}

void print_digits_array(void)
{
  int i, j;

  for (i = 0; i < 4; i++) {
    for (j = 0; j < MAX_DIGITS * 4; j++) {
      printf("%c", digits[i][j]);
    }
    printf("\n");
  }
}
