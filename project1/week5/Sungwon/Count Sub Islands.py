class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m = len(grid1)
        n = len(grid1[0])
        move = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        visited = [[False for _ in range(n)] for _ in range(m)]
        cnt = 0

        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1 and not visited[i][j]:
                    isSubIsland = True
                    stack = [(i, j)]
                    while stack:
                        value = stack.pop()
                        x = value[0]
                        y = value[1]
                        visited[x][y] = True
                        if grid1[x][y] == 0:
                            isSubIsland = False
                        for mo in move:
                            newX = x + mo[0]
                            newY = y + mo[1]
                            if newX >= 0 and newX < m and newY >= 0 and newY < n:
                                if grid2[newX][newY] == 1 and not visited[newX][newY]:
                                    stack.append((newX, newY))
                    if isSubIsland:
                        cnt += 1
                    print('\n')
        return cnt
