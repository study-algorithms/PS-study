class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])

        def getMaxMoney(croppedNums):
            dp = [0] * len(croppedNums)
            dp[0], dp[1] = croppedNums[0], max(croppedNums[0], croppedNums[1])
            
            for i in range(2, len(croppedNums)):
                dp[i] = max(dp[i-2] + croppedNums[i], dp[i-1])
            return dp[len(croppedNums)-1]
        
        return max(getMaxMoney(nums[1:]), getMaxMoney(nums[:-1]))
