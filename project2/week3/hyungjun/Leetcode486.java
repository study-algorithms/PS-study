package project2.week3.hyungjun;

public class Leetcode486 {
    public boolean predictTheWinner(int[] nums) {
        return dfs(0, nums.length - 1, 0, nums, true) > 0 ? true : false;   
    }
    
    private int dfs(int start, int end, int point, int[] nums, boolean isP1) {

        if (start == end) {
            return point;
        }
        if (isP1) {
            int case1 = dfs(start + 1, end, point + nums[start], nums, false);
            int case2 = dfs(start, end - 1, point + nums[end], nums, false);
            return Math.max(case1, case2);
        } else {
            int case1 = dfs(start + 1, end, point - nums[start], nums, true);
            int case2 = dfs(start, end - 1, point - nums[end], nums, true);
            return Math.min(case1, case2);
        }
    }
}
