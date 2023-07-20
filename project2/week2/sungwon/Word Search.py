class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        direction = [(1,0),(0,1),(-1,0),(0,-1)]
        for i in range(len(board)):
            for j in range(len(board[i])):
                stack = []
                visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
                if board[i][j] == word[0]:
                    stack.append((i, j, 0))
                    visited[i][j] = True
                while stack:
                    value = stack.pop()
                    x, y, index = value[0], value[1], value[2]
                    if index == len(word)-1:
                        return True
                    for dir in direction:
                        newX, newY = x+dir[0], y+dir[1]
                        if newX >= 0 and newX < len(board) and newY >= 0 and newY < len(board[0]):
                            if visited[newX][newY] == False and board[newX][newY] == word[index+1]:
                                visited[newX][newY] = True
                                stack.append((newX, newY, index+1))
        return False
