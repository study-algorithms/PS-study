class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        center = [[1,1], [1,4], [1,7], [4,1], [4,4], [4,7], [7,1], [7,4],[7,7]]
        dx, dy = [-1,0,1], [-1,0,1]
        for p in center:
            num = set()
            for y in dy:
                for x in dx:
                    if board[p[0]-x][p[1]-y] != '.':
                        if board[p[0]-x][p[1]-y] not in num:
                            num.add(board[p[0]-x][p[1]-y])
                        else:
                            return False
        for r in range(9):
            num = set()
            for i in range(9):
                if board[r][i] != '.':
                    if board[r][i] not in num:
                        num.add(board[r][i])
                    else:
                        return False
        for c in range(9):
            num = set()
            for i in range(9):
                if board[i][c] != '.':
                    if board[i][c] not in num:
                        num.add(board[i][c])
                    else:
                        return False
        return True
    
