from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        self.word = word
        self.m, self.n = len(board), len(board[0])
        self.visited = [[0] * self.n for _ in range(self.m)]
        self.finish = False
        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] == word[0] and not self.visited[i][j]:
                    self.visited[i][j] = 1
                    self.search(i, j, 0)
                    self.visited[i][j] = 0
        return self.finish

    def search(self, row, col, num):
        print(self.finish, row, col, self.board[row][col], num)
        self.visited[row][col] = 1
        if num == len(self.word)-1 and self.board[row][col] == self.word[num]:
            self.finish = True
            return

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for di in directions:
            if -1< row+di[0] < self.m and -1<col+di[1] < self.n:
                next_t = (row+di[0], col+di[1])
                if num < len(self.word)-1 and not self.visited[next_t[0]][next_t[1]] and self.board[next_t[0]][next_t[1]] == self.word[num+1]:
                    self.search(next_t[0], next_t[1], num+1)
                    self.visited[next_t[0]][next_t[1]] = 0
        
    

                     
# board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# word = "SEE"

# board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# word = "ABCB"

board = [["C","A","A"],["A","A","A"],["B","C","D"]]
word = "AAB"

a = Solution()
print(a.exist(board, word))
