#include <stdio.h>
#include <stdbool.h>

int temperatures[7][24] = {{0}, {0}, {33}, {1}, {0}, {5}, {10}};

bool search(const int a[], int n, int key);

int main(void)
{
  bool result = false;
  int i, (*p)[24];

  for (p = &temperatures[0]; p < &temperatures[7]; p++) {
    if (search(*p, 24, 32)) {
      result = true;
      break;
    }
  }

  if (result) {
    printf("Yes, it has 32 degree one day.\n");
  }
  else {
    printf("Sorry, we don't find this temperature.\n");
  }

  return 0;
}

bool search(const int a[], int n, int key)
{
  int i = 0;

  while (*(a + i) != key && i < n) {
    i++;
  }

  if (i < n) {
    return true;
  }
  else {
    return false;
  }
}
