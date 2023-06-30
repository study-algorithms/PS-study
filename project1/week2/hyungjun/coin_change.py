class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0
        x = [0] * (amount+1)
        for coin in coins:
            if coin <= amount:
                x[coin] = 1
        for i in range(1, amount+1):
            l=[x[i-c] + x[c] for c in coins if (i>c and x[i-c] !=0) or (i==c and x[i-c] == 0)]
            if not len(l):
                l += [0]
            x[i] = min(l)
        return x[amount] if x[amount] else -1
