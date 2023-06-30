class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if self.dfs(board, word, i, j, 0):
                    return True
        return False

    def dfs(self, board, word, x, y, pos):
        if len(word) == pos:
            return True
        # boundary condition
        if x<0 or y<0 or x>=len(board) or y>=len(board[0]) or board[x][y]!=word[pos]:
            return False
        # search
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        temp = board[x][y]
        board[x][y] = -1
        for dx, dy in directions:
            if self.dfs(board, word, x+dx, y+dy, pos+1): 
                return True
        board[x][y] = temp
        return False
