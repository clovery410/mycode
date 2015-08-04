#include <stdio.h>
#include <ctype.h>

#define N 5

float compute_GPA(char grades[], int n);

int main(void)
{
  int i;
  char grades[N];

  printf("Enter grades of %d subjects: ", N);
  for (i = 0; i < N; i++)
    scanf(" %c", &grades[i]);

  printf("The average of the grades is %.2f\n", compute_GPA(grades, N));
  return 0;
}

float compute_GPA(char grades[], int n)
{
  int i;
  float sum = 0.0;
  for (i = 0; i < n; i++)
    switch (toupper(grades[i])) {
    case 'A': sum += 4; break;
    case 'B': sum += 3; break;
    case 'C': sum += 2; break;
    case 'D': sum += 1; break;
    case 'F': sum += 0; break;
    default: break;
    }
    
  return sum / n;
}
