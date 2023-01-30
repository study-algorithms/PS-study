class Solution:
    def findIsland(self, grid: List[List[int]], i, j):
        di, dj = [-1,0,1,0], [0,1,0,-1]
        visited = set()
        def dfs(grid, i, j):
            visited.add((i,j))
            for d_i, d_j in zip(di,dj):
                if i+d_i >= 0 and i+d_i < len(grid) and j+d_j >= 0 and j+d_j < len(grid[0]):
                    if grid[i+d_i][j+d_j] == 1 and (i+d_i, j+d_j) not in visited:
                        dfs(grid, i+d_i, j+d_j)
        dfs(grid, i, j)
        return list(visited)

    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        answer = 0
        islandAllSet = set()
        for i in range(len(grid1)):
            for j in range(len(grid1[0])):
                if (i,j) not in islandAllSet and grid1[i][j] == 1:
                    island = self.findIsland(grid1, i, j)
                    for t in [*island]:
                        islandAllSet.add(t)
        subIslandAllSet = set()
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if (i,j) in islandAllSet and (i,j) not in subIslandAllSet and grid2[i][j] == 1:
                    subIsland = self.findIsland(grid2, i, j)
                    isSubIsland=True
                    for t in [*subIsland]:
                        isSubIsland = isSubIsland and (t in islandAllSet)
                        subIslandAllSet.add(t)
                    if isSubIsland:
                        answer += 1
        return answer
