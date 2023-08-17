class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        self.nums = nums
        self.target = target
        return self.dfs(0)

    @cache
    def dfs(self, cur):
        if cur > self.target:
            return 0

        elif cur == self.target:
            return 1

        else:
            answer = 0
            for n in self.nums:
                answer += self.dfs(cur+n)
        return answer

a = Solution()
print(a.combinationSum4(nums = [1,2,3], target = 4))
# 7
