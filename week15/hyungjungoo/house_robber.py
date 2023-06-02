class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = [0] * (len(nums))
        dp[0], dp[1] = nums[0], nums[1]

        if len(nums) > 2 :
            for i in range(2, len(nums)):
                if i > 2:
                    dp[i] = nums[i] + max(dp[i-2], dp[i-3])
                else:
                    dp[i] = nums[i] + dp[i-2]
        return max(dp[-1], dp[-2])
