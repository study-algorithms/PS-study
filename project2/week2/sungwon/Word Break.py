class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s)+1)
        for word in wordDict:
            if s.startswith(word):
                dp[len(word)] = True

        for i in range(1, len(s)):
            if dp[i]:
                print(i)
                for word in wordDict:
                    if s.startswith(word, i):
                        dp[i+len(word)] = True
        return dp[len(s)]
        
        # bfs => timeout
        # q = deque([0])
        # while q:
        #     i = q.popleft()
        #     wordLeft = s[i:]
        #     for word in wordDict:
        #         if wordLeft.startswith(word):
        #             newI = i + len(word)
        #             if newI == len(s):
        #                 return True
        #             q.append(newI)
        # return False
