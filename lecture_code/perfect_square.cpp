class Solution {
public:
  int numSquares(int n) {
    vector<int> squares;
    for (int i = 1; i * i <= n; i++) squares.push_back(i*i);
    // W = n
    // f(n) = min{ f(n - x) + 1 | x all square numbers}
    vector<int> f(n+1, INT_MAX);
    f[0] = 0;
    for (int i = 1; i <= n; i++)
      for (auto x:squares)
	if (i - x >= 0) f[i] = min(f[i], f[i - x] + 1);
    return f[n];
    
    //12 = 4 + 4 + 4
