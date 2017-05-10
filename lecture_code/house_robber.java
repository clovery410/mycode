public calss Solution {
    public int rob(int[], nums) {
	int n = nums.length;
	int[][] dp = new int[n+1][2];
	//dp[0][c] = 0
	for (int i = 1; i <= n; i++) {
	    dp[i][0] = Math.max(dp[i-1][1], dp[i-1][0]);
	    dp[i][1] = dp[i-1][0] + nums[i - 1];
	}
	return Math.max(dp[n][0], dp[n][1]);
    }
}

