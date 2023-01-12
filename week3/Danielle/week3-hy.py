class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        res_len = 0

        for i in range(len(s)):
            # odd
            l, r = i, i
            while l>=0 and r < len(s) and s[l]==s[r]:
                temp_len = r-l+1
                if temp_len > res_len:
                    res = s[l:r+1]
                    res_len = temp_len
                l -= 1
                r += 1
            # even
            l, r = i, i+1
            while l>=0 and r < len(s) and s[l]==s[r]:
                temp_len = r-l+1
                if temp_len > res_len:
                    res = s[l:r+1]
                    res_len = temp_len
                l -= 1
                r += 1
        
        return res
