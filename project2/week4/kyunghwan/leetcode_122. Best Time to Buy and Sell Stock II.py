class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        l, r = 0, 1
        profit = 0
        while l<= len(prices)-2 and r <= len(prices)-1:
            l_value, r_value = prices[l], prices[r]
            if l_value < r_value:
                profit += (r_value-l_value)
            
            l, r = r, r+1

        
        return profit


a = Solution()
print(a.maxProfit([7,1,5,3,6,4]))
# 7
