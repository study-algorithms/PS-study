class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:        
        list = [amount+1] * (amount+1)
        list[0] = 0

        for coin in coins:
            for i in range(coin, amount+1):
                list[i] = min(list[i], list[i-coin]+1)

        if list[amount] != amount+1:
            return list[amount]
        return -1
