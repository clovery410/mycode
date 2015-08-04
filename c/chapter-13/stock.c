#include <stdio.h>

#define N 5

int trend[N] = {3, 4, 5, 1, 2};

int stock(int trend[], int n, int p);

int main(void)
{
  int i, revenue, sell, buy;

  buy = trend[0];
  sell = stock(trend, N, 0);
  revenue = sell - buy;
  for (i = 1; i < N - 1; i++) {
    if (trend[i] < buy) {
      if (stock(trend, N, i) - trend[i] > revenue) {
        buy = trend[i];
	sell = stock(trend, N, i);
	revenue = sell - buy;
      }
    }
  }

  printf("You should buy at %d, and sell at %d, then revenue is: %d\n", buy, sell, revenue);

  return 0;
}

int stock(int trend[], int n, int p)
{
  int i, sell;

  sell = trend[p+1];
  for (i = p; i < n; i++) {
    if (trend[i] > sell)
      sell = trend[i];
  }
  return sell;
}
