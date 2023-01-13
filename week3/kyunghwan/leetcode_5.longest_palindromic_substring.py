s = "babad"
class Solution:
    def longestPalindrome(self, s: str) -> str:
        odd = ''
        even = ''
        for i in range(len(s)):
            # odd
            left, right = i, i
            while -1 < left and right < len(s):
                if s[left] == s[right]:
                    left-=1
                    right+=1
                else:
                    break
            if len(s[left+1 : right]) > len(odd):
                odd = s[left+1 : right]

            # even
            left, right = i, i+1
            while -1 < left and right < len(s):
                if s[left] == s[right]:
                    left-=1
                    right+=1
                else:
                    break

            if len(s[left+1 : right]) > len(even):
                even = s[left+1 : right]

        if len(odd) > len(even):
            return odd

        else:
            return even


test =Solution()
print(test.longestPalindrome(s))

    
     
    