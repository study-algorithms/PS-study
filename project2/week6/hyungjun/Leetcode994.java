class Solution {
    public int orangesRotting(int[][] grid) {
        int[] di = new int[]{-1, 0, 1, 0};
        int[] dj = new int[]{0, -1, 0, 1};
        List<int[]> rottenOranges = new ArrayList<>();
        int freshOrangeCount = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == 2){
                    rottenOranges.add(new int[]{i, j});
                }
                if (grid[i][j] == 1) {
                    freshOrangeCount += 1;
                }
            }
        }
        int min = 0;
        while (freshOrangeCount > 0) {
            min += 1;
            int rottenOrangeCount = 0;
            List<int[]> newRottenOranges = new ArrayList<>();
            for (int[] rottenOrange : rottenOranges) {
                int i = rottenOrange[0];
                int j = rottenOrange[1];
                for (int d = 0; d < 4; d++) {
                    if (i + di[d] < grid.length && i + di[d] >= 0 && j + dj[d] < grid[0].length && j + dj[d] >= 0) {
                        if (grid[i+di[d]][j+dj[d]] == 1) {
                            grid[i+di[d]][j+dj[d]] = 2;
                            rottenOrangeCount += 1;
                            newRottenOranges.add(new int[]{i+di[d], j+dj[d]});
                        }
                    }
                }
            }
            rottenOranges.addAll(newRottenOranges);
            if (rottenOrangeCount == 0) {
                break;
            }
            freshOrangeCount -= rottenOrangeCount;
        }
        if (freshOrangeCount > 0) {
            return -1;
        }
        return min;
    }
}
