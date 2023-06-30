class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot = self.findPivot(nums)
        return max(self.binarySearch(nums, target, 0, pivot-1), self.binarySearch(nums, target, pivot, len(nums)-1))

    def binarySearch(self, nums, target, left, right):
        while left <= right:
            mid = (left+right)//2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid-1
            else:
                left = mid+1
        return -1

    def findPivot(self, nums):
        left = 0
        right = len(nums)-1

        if len(nums) == 1:
            return 0
        if nums[left] < nums[right]:
            return 0

        while left < right:
            mid = (left+right)//2
            
            if nums[mid] > nums[right]:
                left = mid+1
            else:
                right = mid
        return left
