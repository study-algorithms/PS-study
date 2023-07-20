class Solution {
public:
    bool backtrack(vector<vector<char>>& board, string word, int x, int y, int row, int col, int index) {
        // if true, traversed all characters of 'word'
        if (index == word.size())
            return true;

        // checks if row or col are out of bounds
        // checks if character at [row][col] position of board not the same as word[index]
        if (row < 0 || row >= x || col < 0 || col >= y || board[row][col] != word[index])
            return false;

        char temp = board[row][col];
        board[row][col] = '*';
        // traverse all four directions
        bool sol1 = backtrack(board, word, x, y, row + 1, col, index+1);
        bool sol2 = backtrack(board, word, x, y, row, col + 1, index+1);
        bool sol3 = backtrack(board, word, x, y, row - 1, col, index+1);
        bool sol4 = backtrack(board, word, x, y, row, col - 1, index+1);
        // change cell back to temp to backtrack and make cell available for other paths
        board[row][col] = temp;
        return sol1 || sol2 || sol3 || sol4;
    }

    bool exist(vector<vector<char>>& board, string word) {
        int x = board.size();
        int y = board[0].size();
        for (int i = 0; i < x; i++) {
            for (int j = 0; j < y; j++) {
                if (backtrack(board, word, x, y, i, j, 0))
                    return true;
            }
        }
        return false;
    }
};

// Time Complexity O(NM4^L)
// Space Complexity O(L)
