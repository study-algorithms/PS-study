class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        for i in range(len(nums)-2):
            l, r = i+1, len(nums)-1
            while l < r:
                sum = nums[l]+nums[r]+nums[i]
                if sum == 0:
                    ans.append((nums[l], nums[r], nums[i]))
                    l += 1
                    r -= 1
                elif sum < 0:
                    l += 1
                else:
                    r -= 1

        return list(set(ans))
