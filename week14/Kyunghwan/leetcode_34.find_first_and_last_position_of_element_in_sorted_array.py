from typing import *

nums = [5,7,7,8,8,10]
target = 8

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        answer = [-1,- 1]
        idx =[]
        if nums:
            for i in range(len(nums)):
                if nums[i] == target :
                    idx.append(i)
                    break

            for j in range(len(nums)-1, -1, -1):
                if nums[j] == target :
                    idx.append(j)
                    break
        if idx:
            answer[0], answer[1] = min(idx), max(idx)

        return answer
    

a = Solution()
print(a.searchRange(nums, target))
