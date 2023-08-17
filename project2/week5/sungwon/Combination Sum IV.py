class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * 1001
        for num in nums:
            dp[num] = 1
        for i in range(1, target+1):
            if dp[i] != 0:
                for num in nums:
                    if i+num <= target:
                        dp[i+num] += dp[i]
        return dp[target]
