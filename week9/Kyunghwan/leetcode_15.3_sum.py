nums = [-1,0,1,2,-1,-4]
class Solution:
    def threeSum(self, nums):
        nums = sorted(nums)
        output = []
        for i in range(len(nums)-2):
            left, right = i+1, len(nums)-1
            while left < right:
                sums = nums[i] + nums[left] + nums[right]
                if sums > 0 :
                    right-=1
                elif sums < 0:
                    left+=1
                else:
                    if [nums[i], nums[left], nums[right]] not in output:
                        output.append([nums[i], nums[left], nums[right]])

                    left+=1
                    right-=1

        return output


a = Solution()
print(a.threeSum(nums))