class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        mini = nums[0]

        while left <= right :
            if nums[left] < nums[right]:
                mini= min(nums[left], mini)
                break

            mid = left+right //2
            mini = min(mini, nums[mid])

            if nums[left] <= nums[mid]:
                left+=1
            else:
                right-=1

        return mini


a = Solution()
print(a.findMin([4,5,6,7,0,1,2]))
# 0 
