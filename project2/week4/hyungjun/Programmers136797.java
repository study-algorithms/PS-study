package project2.week4.hyungjun;


public class Programmers136797 {
    
    private int[][] dist = new int[10][10];
    private int[][][] dp;

    public int solution(String numbers) {
        setDistance();
        dp = new int [numbers.length()][10][10];
        return dfs(numbers, 0, 4, 6);
    }
    private int dfs(String numbers, int index, int left, int right) {

        if (index == numbers.length()) {
            return 0;
        }
        int number = numbers.charAt(index) - '0';
        if (dp[index][left][right] != 0) {
            return dp[index][left][right];
        }
        int result = Integer.MAX_VALUE;
        
        if (number != right) {
            result = Math.min(result, dfs(numbers, index+1, number, right) + dist[left][number]);
        }
        if (number != left) {
            result = Math.min(result, dfs(numbers, index+1, left, number) + dist[right][number]);
        }
        dp[index][left][right]=result;
        return result;
    }


    private void setDistance() {
        for (int i = 0; i < dist.length; i++) {
            for (int j = 0; j < dist.length; j++) {
                if (i == j) {
                    dist[i][j] = 1;
                    continue;
                }
                if (dist[i][j] != 0) {
                    continue;
                }
                int ri, ci, rj, cj; // row of i, column of i
                if (i == 0) {
                    ri = 3;
                    ci = 1;
                } else {
                    ri = (i-1) / 3;
                    ci = (i-1) % 3;
                }
                if (j == 0) {
                    rj = 3;
                    cj = 1;
                } else {
                    rj = (j-1) / 3;
                    cj = (j-1) % 3;
                }

                int dr = ri > rj ? (ri-rj) : (rj-ri);
                int dc = ci > cj ? (ci-cj) : (cj-ci);
                if (dr + dc == 1) {
                    dist[i][j] = 2;
                    dist[j][i] = 2;
                    continue;
                }

                dist[i][j] = 2*(dr > dc ? dr : dc) + (dr > dc ? dc : dr);
                dist[j][i] = dist[i][j];
            }
        }
    }
    public static void main(String[] args) {
        Programmers136797 programmers136797 = new Programmers136797();
        programmers136797.solution("1756");
    }
}

// {1,2,3}
// {4,5,6}
// {7,8,9}
// {*,0,*}
