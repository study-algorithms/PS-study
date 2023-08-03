class Solution:
    def dp(self, target:List[int])-> int:
        dp = [0] * len(target)
        dp[0], dp[1] = target[0], max(target[0], target[1])
        for i in range(2, len(target)):
            dp[i] = max(dp[i-1], dp[i-2]+target[i])
        return dp[-1]

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) ==2:
            return max(nums[0], nums[1])
        else:
            
            first_start = nums[:len(nums)-1]
            second_start = nums[1:len(nums)]

            return max(self.dp(first_start), self.dp(second_start))

a = Solution()
print(a.rob([1,2,3,1]))
# 4
