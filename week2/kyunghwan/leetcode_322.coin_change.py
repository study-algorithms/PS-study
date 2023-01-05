coins = [1, 2, 5]
amount = 11


class Solution:
    def coinChange(self, coins, amount):

        if amount == 0:
            return 0 

        q = [0]
        visited = [0] * (amount+1)
        visited[0] = 1
        cnt = 0

        while q:
            cnt+=1
            avail = []
            for num in q:
                for coin in coins:
                    newnum = num + coin
                    if newnum == amount:
                        return cnt
                    if newnum > amount:
                        continue
                    if not visited[newnum]:
                        visited[newnum] = 1
                        avail.append(newnum)
            q = avail

        return -1



a =Solution()
print(a.coinChange(coins, amount))

# print([2**3-1]*4) 