import math
class Solution(object):
    # def uniquePaths(self, m, n):
    #     """
    #     :type m: int
    #     :type n: int
    #     :rtype: int
    #     """
    #     if m == 1 and n ==1 :
    #         return 1
    #     directions = [(1, 0), (0, 1)]
    #     queue = [(0, 0)]
    #     answer = 0
    #     while queue:
    #         cur = queue.pop(0)
    #         for di in directions:
    #             nexts = (cur[0]+di[0], cur[1]+di[1])
    #             if nexts == (m-1, n-1):
    #                 answer+=1
    #             if -1< nexts[0] < m and -1 < nexts[1] < n :
    #                 queue.append(nexts)
    #     return answer

    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
    
        return math.factorial(m+n-2) / (math.factorial(m-1) * math.factorial(n-1))

a = Solution()
print(a.uniquePaths(m = 3, n = 7))
# 28
