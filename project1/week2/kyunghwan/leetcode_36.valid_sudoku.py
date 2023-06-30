board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

class Solution:
    def isValidSudoku(self, board: list) -> bool:
        garo = [[] for _ in range(9)]
        sero = [[] for _ in range(9)]
        box = [[] for _ in range(9)]
        idx = {'[0, 0]':0, '[0, 1]': 1, '[0, 2]':2, 
        '[1, 0]':3, '[1, 1]': 4, '[1, 2]':5, 
        '[2, 0]':6, '[2, 1]': 7, '[2, 2]':8 }

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue

                if board[i][j] in garo[i]:
                    return False

                if board[i][j] in sero[j]:
                    return False

                
                if board[i][j] in box[idx[str([i//3, j//3])]]:
                    return False
                

                garo[i].append(board[i][j])
                sero[j].append(board[i][j])
                box[idx[str([i//3, j//3])]].append(board[i][j])
        return True

    
a= Solution()
print(a.isValidSudoku(board))

            




            