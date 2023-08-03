class Solution:
    def partitionString(self, s: str) -> int:
        check = [0] * 26
        check[ord(s[0])-97] =1
        cnt = 1
        for letter in s[1:]:
            if check[ord(letter)-97]:
                cnt+=1
                check = [0] * 26
                check[ord(letter)-97] = 1
            check[ord(letter)-97] = 1
        return cnt

a = Solution()
print(a.partitionString("abacaba"))
# 4
