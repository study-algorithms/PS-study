from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, maxLen, maxFreq = 0, 0, 0
        c = collections.Counter()
        for right in range(len(s)):
            c[s[right]] += 1
            maxFreq = max(maxFreq, c[s[right]])
            if right-left+1-maxFreq > k:
                c[s[left]] -= 1
                left += 1
            maxLen = max(maxLen, right-left+1)
        return maxLen
