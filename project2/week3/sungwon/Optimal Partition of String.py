class Solution:
    def partitionString(self, s: str) -> int:
        ss = set()
        ans = 0

        for ch in s:
            if ch not in ss:
                ss.add(ch)
            else:
                ss.clear()
                ss.add(ch)
                ans += 1
        return ans+1
