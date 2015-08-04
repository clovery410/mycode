#include <stdio.h>
#include <stdbool.h>

int main(void)
{
  bool digit_seen[10] = {false};
  bool repeat = false;
  int digit;
  long n;

  printf("Enter a number: ");
  scanf("%ld", &n);

  printf("Repeated digit(s):");
  while (n > 0) {
    digit = n % 10;
    if (digit_seen[digit]) {
      repeat = true;
      printf(" %d", digit);
    }
    else 
      digit_seen[digit] = true;
    n /= 10;
  }

  if (repeat)
    printf("\n");
  else
    printf(" No repeated digit\n");

  return 0;
}
