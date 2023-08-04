package project2.week3.hyungjun;

public class Leetcode213 {
    public int rob(int[] nums) {
        
        int[] robWithFirst = new int[nums.length];
        int[] robWithOutFirst = new int[nums.length];

        robWithFirst[0] = nums[0];
        if (nums.length == 1) {
            return nums[0];
        }
        if (nums.length == 2) {
            return (nums[0] >= nums[1]) ? nums[0] : nums[1];
        }
        robWithFirst[1] = nums[0];
        for (int i = 2; i < nums.length; i++) {
            if (i == nums.length - 1) {
                robWithFirst[i] = robWithFirst[i-1];
            } else {
                robWithFirst[i] = (robWithFirst[i-1] >= robWithFirst[i-2] + nums[i]) ? robWithFirst[i-1] : robWithFirst[i-2] + nums[i];
            }
        }

        robWithOutFirst[1] = nums[1];
        for (int i = 2; i < nums.length; i++) {
            robWithOutFirst[i] = (robWithOutFirst[i-1] >= robWithOutFirst[i-2] + nums[i]) ? robWithOutFirst[i-1] : robWithOutFirst[i-2] + nums[i];
        }

        return (robWithFirst[nums.length-1] >= robWithOutFirst[nums.length-1]) ? robWithFirst[nums.length - 1] : robWithOutFirst[nums.length-1];
    }
}
