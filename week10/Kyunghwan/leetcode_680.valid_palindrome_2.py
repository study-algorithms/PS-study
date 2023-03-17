
# s = "abca"
# s = "abc"
s = "aba"
class Solution:
    def validPalindrome(self, s):
        left, right = 0, len(s)-1
        while left<right:
            if s[left] != s[right]:
                break
            left+=1
            right-=1

        if left>=right:
            return True


        left, right, chance = 0, len(s)-1, 1

        while left<right:
            if s[left] != s[right] and chance:
                left+=1
                chance = 0
                continue
            elif s[left] != s[right] and not chance:
                break
            left+=1
            right-=1

        if left>=right:
            return True

        
        left, right, chance = 0, len(s)-1, 1

        while left<right:
            if s[left] != s[right] and chance:
                right-=1
                chance = 0
                continue
            elif s[left] != s[right] and not chance:
                break
            left+=1
            right-=1

        if left>=right:
            return True

        
        return False

a=Solution()
print(a.validPalindrome(s))