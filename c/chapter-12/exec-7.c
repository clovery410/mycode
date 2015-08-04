#include <stdio.h>
#include <stdbool.h>

#define N 10
const int a[N] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

bool search(const int a[], int n, int key);

int main(void)
{
  int key;
  bool result;

  printf("Enter keyword (a number) to search: ");
  scanf("%d", &key);
  result = search(a, N, key);

  if(result) {
    printf("Yes, we have corresponding results.\n");
  }
  else {
    printf("Sorry, we don not have corresponding search results\n");
  }

  return 0;
}
bool search(const int a[], int n, int key)
{
  int *p;
  p = a;

  while (*p != key && p < a + n) {
    p++;
  }

  if (p < a + n) {
    return true;
  }
  else {
    return false;
  }
}
