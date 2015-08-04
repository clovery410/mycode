#include <stdio.h>

int main(void)
{
  int one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen;
  int row_sum1, row_sum2, row_sum3, row_sum4, col_sum1, col_sum2, col_sum3, col_sum4, dia_sum1, dia_sum2;

  printf("Enter the numbers from 1 to 16 in any order:\n");
  scanf("%d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d", &one, &two, &three, &four, &five, &six, &seven, &eight, &nine, &ten, &eleven, &twelve, &thirteen, &fourteen, &fifteen, &sixteen);

  row_sum1 = one + two + three + four;
  row_sum2 = five + six + seven + eight;
  row_sum3 = nine + ten + eleven + twelve;
  row_sum4 = thirteen + fourteen + fifteen + sixteen;
  col_sum1 = one + five + nine + thirteen;
  col_sum2 = two + six + ten + fourteen;
  col_sum3 = three + seven + eleven + fifteen;
  col_sum4 = four + eight + twelve + sixteen;
  dia_sum1 = one + six + eleven + sixteen;
  dia_sum2 = four + seven + ten + thirteen;

  printf("%2d %2d %2d %2d\n", one, two, three, four);
  printf("%2d %2d %2d %2d\n", five, six, seven, eight);
  printf("%2d %2d %2d %2d\n", nine, ten, eleven, twelve);
  printf("%2d %2d %2d %2d\n\n", thirteen, fourteen, fifteen, sixteen);

  printf("Row sums: %d %d %d %d\n", row_sum1, row_sum2, row_sum3, row_sum4);
  printf("Column sums: %d %d %d %d\n", col_sum1, col_sum2, col_sum3, col_sum4);
  printf("Diagonal sums: %d %d\n", dia_sum1, dia_sum2);

  return 0;
}
