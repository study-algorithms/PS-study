class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        vector<int> dir = {-1, 0, 1, 0, -1};

        int n = grid.size();
        int m = grid[0].size();

        queue<pair<int, int>> q;
        int count = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == 2) q.push({i, j});
                if (grid[i][j] == 1) count++;
            }
        }
        int ans = -1;
        while (!q.empty()) {
            int len = q.size();
            while(len--) {
                pair<int, int> p = q.front();
                q.pop();
                for (int i = 0; i < 4; i++) {
                    int row = p.first + dir[i];
                    int col = p.second + dir[i+1];
                    if (row >= 0 && row < n && col >= 0 && col < m && grid[row][col] == 1) {
                        grid[row][col] = 2;
                        q.push({row, col});
                        count--;
                    }
                }
            }
            ans++;
        }
        if (count > 0) return -1;
        if (ans == -1) return 0;
        return ans;
    }
};
