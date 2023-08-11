class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0]*n for _ in range(m)]

        if m==1 or n==1:
            return 1

        for i in range(n):
            grid[0][i] = 1
        for i in range(m):
            grid[i][0] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = grid[i-1][j] + grid[i][j-1]
        
        return grid[m-1][n-1]

# 1  1  1  1  1  1  1
# 1  2  3  4  5  6  7
# 1  3  6  10 15 21 28 
