class Solution:
    def longestPalindrome(self, s: str) -> str:
        answer = s[0]

        for i in range(len(s)):
            for j in range(len(s)-1, i, -1):
                k = i
                l = j
                found = True
                while k < l:
                    if s[k] != s[l]:
                        found = False
                        break
                    k += 1
                    l -= 1
                if found:
                    if j-i+1 > len(answer):
                        answer = s[i:j+1]
                    break

        return answer
