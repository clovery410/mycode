#include <stdio.h>
#include <string.h>

int main(void)
{
  int n;
  char *tens[] = {"ten", "eleven", "twelve", "thirteen", "fourteen",
			      "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"};
  char *first_digit[] = {"twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"};
  char *second_digit[] = {"", "-one", "-two", "-three", "-four", "-five", "-six", "-seven", "-eight", "-nine"};

  printf("Enter a two-digit number: ");
  scanf("%d", &n);

  printf("You entered the number ");
  if (n / 10 == 1)
    printf("%s\n", tens[n % 10]);
  else if (n / 10 <= 0 || n / 10 >= 10)
    printf("Please enter two-digit number.\n");
  else {
    printf("%s%s\n", first_digit[n / 10 - 2], second_digit[n % 10]);
  }

  return 0;
}
