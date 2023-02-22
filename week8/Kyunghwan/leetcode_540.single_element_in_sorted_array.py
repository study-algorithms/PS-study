nums = [3,3,7,7,10,11,11]
# nums = [1,1,2,3,3,4,4,8,8]
# nums = [1]
# nums = [1,1,2,2,3]

class Solution:
    def singleNonDuplicate(self, nums):
        if len(nums)== 1:
            return nums[0]
        
        while True:
            if len(nums) == 3:
                if nums[0] == nums[1]:
                    answer = nums[2]
                else:
                    answer = nums[0]
                break
            else:
                center = len(nums)//2
                if nums[center] == nums[center-1]:
                    left, right = nums[:center+1], nums[center+1:]
                    if len(left) % 2:
                        nums = left[:]
                    else:
                        nums = right[:]
                elif nums[center] == nums[center+1]:
                    left, right = nums[:center], nums[center:]
                    if len(left) % 2:
                        nums = left[:]
                    else:
                        nums = right[:]
                else:
                    answer = nums[center]
                    break
        return answer

a = Solution()
print(a.singleNonDuplicate(nums))