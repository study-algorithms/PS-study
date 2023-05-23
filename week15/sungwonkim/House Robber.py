class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0 for _ in range(len(nums))]

        if len(nums) == 1:
            return nums[0]
        
        dp[0] = nums[0]
        if nums[0] <= nums[1]:
            dp[1] = nums[1]
        else:
            dp[1] = nums[0]

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        return max(dp[len(nums)-1], dp[len(nums)-2])
