nums = [3,2,1,0,4]

class Solution:
    def canJump(self, nums) -> bool:
        arrive = len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            if i+nums[i] >= arrive:
                arrive = i
        
        if arrive == 0:
            return True
        else:
            return False


a= Solution()
print(a.canJump(nums))