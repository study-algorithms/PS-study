# O(n2)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        x = [[0]*len(s) for _ in range(len(s))]
        left,right, maxlen = 0,0,0
        for i in range(len(s)-1,-1,-1):
            for j in range(i, len(s)):
                if i == j:
                    x[i][j] = 1
                elif s[i] == s[j]:
                    if j == i+1:
                        x[i][j] = 1
                    else:
                        x[i][j] = x[i+1][j-1]
                if x[i][j] and maxlen < j-i+1:
                    left, right, maxlen = i, j, j-i+1
        return s[left:right+1]

# O(n)
# reference (https://www.scaler.com/topics/data-structures/manachers-algorithm/)
class Solution2:

    # Implementation of Manacher's Algorithm
    def longestPalindrome(self, s):

        # If length of given string is n then its length after
        # inserting n+1 "#", one "@", and one "$" will be
        # (n) + (n+1) + (1) + (1) = 2n+3
        strLen = 2 * len(s) + 3
        sChars = [0]*strLen

        # Inserting special characters to ignore special cases
        # at the beginning and end of the array
        # "abc" -> @ # a # b # c # $
        # "" -> @#$
        # "a" -> @ # a # $
        sChars[0] = '@'
        sChars[strLen - 1] = '$'
        t = 1
        for i in s:
            sChars[t] = '#'
            t += 1
            sChars[t] = i
            t += 1

        sChars[t] = '#'

        maxLen = int(0)
        start = int(0)
        maxRight = int(0)
        center = int(0)
        p = [0] * strLen  # i's radius, which doesn't include i
        for i in range(1, strLen - 1):
            if i < maxRight:
                p[i] = min(maxRight - i, p[2 * center - i])

            # Expanding along the center
            while sChars[i + p[i] + 1] == sChars[i - p[i] - 1]:
                p[i] += 1

            # Updating center and its bound
            if i + p[i] > maxRight:
                center = i
                maxRight = i + p[i]

            # Updating ans
            if p[i] > maxLen:
                start = int((i - p[i] - 1) / 2)
                maxLen = p[i]

        # printSubstring(s, start, start + maxLen - 1)
        return s[start: start+maxLen]
