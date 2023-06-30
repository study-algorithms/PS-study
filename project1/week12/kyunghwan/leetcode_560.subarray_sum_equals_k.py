nums = [1,2,3]
k = 3

class Solution:
    def subarraySum(self, nums, k):
        sums = {0:1}
        ans, tot = 0, 0
        for i in range(len(nums)):
            tot += nums[i]
            if tot - k in sums:
                ans += sums[tot-k]
            if tot in sums:
                sums[tot] += 1
            else:
                sums[tot] = 1
        return ans
   

a = Solution()
print(a.subarraySum(nums, k))