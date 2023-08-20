package project2.week6.hyungjun;

/**
 * Leetcode153
 */
public class Leetcode153 {
    public int findMin(int[] nums) {
        int l = 0;
        int r = nums.length - 1;
        while (l < r) {
            int mid = (l + r) / 2;
            if (nums[l] <= nums[mid] && nums[mid] < nums[r]) {
                return nums[l];
            }
            if (nums[l] <= nums[mid] && nums[mid] > nums[r]) {
                l = mid + 1;
                continue;
            }
            if (nums[l] >= nums[mid] && nums[mid] < nums[r]) {
                r = mid;
            }
        }

        return nums[l];
    }
}