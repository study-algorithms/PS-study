class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)-1

        if len(nums) == 1:
            return nums[0]

        while low <= high:
            mid = (low + high)//2

            index = self.checkSingle(nums, mid)
            if index == -1:
                return nums[mid]
            if index%2 == 0:
                high = mid-1
            else:
                low = mid+1
        

    def checkSingle(self, nums, mid):
        if mid == 0:
            if nums[mid] == nums[mid+1]:
                return mid+1
        elif mid == len(nums)-1:
            if nums[mid] == nums[mid-1]:
                return mid
        else:
            if nums[mid] == nums[mid+1]:
                return mid+1
            elif  nums[mid] == nums[mid-1]:
                return mid
        return -1
