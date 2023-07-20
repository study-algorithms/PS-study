bool dfs(vector<vector<char>>& board, string word, int i, int j, int k) {
    // check if current coordinates are out of grid or the current cell doesn't match the current character of the word
    if (i < 0 || i >= board.size() || j < 0 || j >= board[0].size() || board[i][j] != word[k]) {
        return false;
    }
    // check if we have reached the end of the word
    if (k == word.length() - 1) {
        return true;
    }
    // mark the current cell as visited by replacing it with '/'
    char tmp = board[i][j];
    board[i][j] = '/';
    // check all 4 adjacent cells recursively
    bool res = dfs(board, word, i+1, j, k+1) ||
              dfs(board, word, i-1, j, k+1) ||
              dfs(board, word, i, j+1, k+1) ||
              dfs(board, word, i, j-1, k+1);
    // backtrack by replacing the current cell with its original value
    board[i][j] = tmp;
    return res;
}

bool exist(vector<vector<char>>& board, string word) {
    for (int i = 0; i < board.size(); i++) {
        for (int j = 0; j < board[0].size(); j++) {
            // start the search from every cell
            if (dfs(board, word, i, j, 0)) {
                return true;
            }
        }
    }
    return false;
}

/*
Time Complexity: O(4^N)
Space Complexity: O(N)
*/
