#include <stdio.h>

int main(void)
{
  int score, ten;

  printf("Enter numerical grade: ");
  scanf("%d", &score);
  
  if (score > 100 || score < 0)
    printf("Invalid grade\n");

  ten = score / 10;
  
  switch (ten) {
  case 10: 
  case 9: printf("A"); break;
  case 8: printf("B"); break;
  case 7: printf("C"); break;
  case 6: printf("D"); break;
  default: printf("F"); break;
  }
  printf("\n");
  return 0;
}
