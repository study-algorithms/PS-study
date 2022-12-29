class Solution(object):
    def productExceptSelf(self, nums):
        ans = []
        temp = 1
        for i in range(0, len(nums)):
            ans.append(temp)
            temp *= nums[i]
        
        temp = 1
        for i in range(len(nums)-1, -1, -1):
            ans[i] *= temp
            temp *= nums[i]

        return ans
