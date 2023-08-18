func combinationSum4(nums []int, target int) int {
	dp := []int{}
	for i := 0; i <= target; i++ {
		dp = append(dp, 0)
	}
	for _, v := range nums {
		if v <= target {
			dp[v] = 1
		}
	}

	for i := 0; i <= target; i++ {
		for _, v := range nums {
			if i-v > 0 {
				dp[i] += dp[i-v]
			}
		}
	}
	return dp[target]
}
