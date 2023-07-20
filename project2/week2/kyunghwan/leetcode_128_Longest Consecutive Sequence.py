class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        longest = 1
        nums = set(nums)
        for num in nums:
            if num-1 not in nums:
                cnt = 1
                next_n = num+1
                while next_n in nums:
                    next_n+=1
                    cnt+=1
                if cnt > longest:
                    longest = cnt
        return longest

a = Solution()
print(a.longestConsecutive([100,4,200,1,3,2]))
# 4
