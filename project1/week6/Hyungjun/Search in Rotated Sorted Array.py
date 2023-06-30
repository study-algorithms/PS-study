import math

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find pivot
        l, r = 0, len(nums)-1
        pivot = 0
        while l != r:
            mid = (l+r)//2
            if not (nums[l] <= nums[mid] and nums[mid] <= nums[r]):
                if nums[mid] > nums[r]:
                    l = mid if nums[l] != nums[mid] else mid + 1
                    pivot = l
                else:
                    r = mid
            else:                
                break
        n_nums = nums[pivot:] + nums[:pivot]
        # find target
        l, r = 0, len(nums)-1
        while l != r:
            mid = math.ceil((l+r)/2)
            if n_nums[mid] > target:
                r = mid - 1
            else:
                l = mid
        if n_nums[l] == target:
            return (pivot + l)%len(nums)
        return -1
