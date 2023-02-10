nums = [1,2,3,4,5,6,7]
k = 3
class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        rot = k% len(nums)
        nums[:] = nums[-rot:] + nums[:-rot]

a = Solution(nums, k)
a.rotate()