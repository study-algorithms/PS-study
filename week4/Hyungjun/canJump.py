class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last = len(nums)-1
        if last == 0:
            return True
        ret = False
        for i in range((len(nums) - 2), -1, -1):
            if nums[i] >= (last - i):
                last = i
                ret = True
            else:
                ret = False
        return ret
