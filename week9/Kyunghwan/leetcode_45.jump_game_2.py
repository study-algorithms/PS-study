class Solution:
    def jump(self, nums):
        check = [0] * len(nums)

        for i in range(len(nums)):
            for j in range(i+1, i+1+nums[i]):
                if j >= len(nums):
                    break
                if check[j] == 0:
                    check[j] = check[i]+1
                
                
        return check[-1]  

nums = [2,3,1,1,4]

a = Solution()
print(a.jump(nums))