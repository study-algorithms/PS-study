class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for x in range(9):
            for y in range(9):
                if board[x][y] != "." and not self.check(x, y, board[x][y], board):
                    return False
        return True

    def check(self, x, y, val, board):
        if self.checkX(x, y, val, board) and self.checkY(x, y, val, board) and self.checkSquare(x, y, val, board):
            return True
        return False

    def checkX(self, x, y, val, board):
        for i in range(9):
            if i != y and board[x][i] == val:
                return False
        return True

    def checkY(self, x, y, val, board):
        for i in range(9):
            if i != x and board[i][y] == val:
                return False
        return True

    def checkSquare(self, x, y, val, board):
        firstX = x//3 * 3
        firstY = y//3 * 3
        for i in range(firstX, firstX+3):
            for j in range(firstY, firstY+3):
                if i != x and j != y and board[i][j] == val:
                    return False
        return True
