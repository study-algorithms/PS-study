type rowColKey [2]int

func exist(board [][]byte, word string) bool {

    for row := 0; row < len(board); row++ {
        for col := 0; col < len(board[0]); col++ {
            if board[row][col] == word[0] {
                visited := make(map[rowColKey]bool)
                visited[rowColKey{row, col}] = true
                if result := findWord(board, row, col, word, 1, visited); result == true {
                    return true
                }
                
            }
        }
        
    }
    return false
}

func findWord(board [][]byte, row, col int, word string, i int, visited map[rowColKey]bool) bool {
    if i == len(word) {
        return true
    }
    dRow := [4]int{-1,0,1,0}
    dCol := [4]int{0,1,0,-1}

    for d := 0; d < 4; d++ {
        if (row + dRow[d] >= 0) && (row + dRow[d] < len(board)) && (col + dCol[d] >= 0) && (col + dCol[d] < len(board[0])) {
            if val, ok := visited[rowColKey{row+dRow[d], col+dCol[d]}]; !ok || val==false {
                if board[row+dRow[d]][col+dCol[d]] == word[i] {
                    visited[rowColKey{row+dRow[d], col+dCol[d]}] = true
                    if result := findWord(board, row+dRow[d], col+dCol[d], word, i+1, visited); result == true {
                        return true
                    }
                    visited[rowColKey{row+dRow[d], col+dCol[d]}] = false
                }
            } 
        }
    }
    return false
}
