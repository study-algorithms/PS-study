class Solution:
    def validPalindrome(self, s: str) -> bool:
        for i in range(len(s)//2+1):
            if s[i] != s[-i]:
                print(i, s)
                i1 = i
                i2 = len(s)-1-i
                str1 = s[:i1] + s[i1+1:]
                str2 = s[:i2] + s[i2+1:]
                #print(str1, str2)
                return str1 == str1[::-1] or str2 == str2[::-1]
        return True
