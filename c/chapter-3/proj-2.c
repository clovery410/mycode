#include <stdio.h>

int main(void)
{
  int num, day, month, year;
  float unit_price;

  printf("Enter item number: ");
  scanf("%d", &num);
  printf("Enter unit price: ");
  scanf("%f", &unit_price);
  printf("Enter purchase date (mm/dd/yyyy): ");
  scanf("%d/%d/%d", &month, &day, &year);

  printf("Item\t\tUnit\t\tPurchase\n");
  printf("\t\tPrice\t\tDate\n");
  printf("%-d\t\t$%7.2f\t%.2d/%.2d/%d\n", num, unit_price, month, day, year);

  return 0;
}
