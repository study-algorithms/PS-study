class Solution:
    def trailingZeroes(self, n: int) -> int:
        cnt = 0
        while n> 0:
            cnt+= (n//5)
            n = n//5
        return cnt


a = Solution()
print(a.trailingZeroes(5))