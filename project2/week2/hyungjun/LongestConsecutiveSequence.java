package project2.week2.hyungjun;

import java.util.HashSet;
import java.util.Set;

class Solution {
    public int longestConsecutive(int[] nums) {
        if (nums.length == 0) {
            return 0;
        }
        Set<Integer> numSet = new HashSet<>();
        Set<Integer> isChecked = new HashSet<>();
        Integer minNum = Integer.MAX_VALUE;
        for (int num : nums) {
            numSet.add(Integer.valueOf(num));
            minNum = Integer.min(minNum, num);
        }
        isChecked.add(minNum);
        int length = 1;
        while (numSet.contains(++minNum)){
            length++;
        }
        
        for (Integer num : numSet) {
            if (!isChecked.contains(num)){
                isChecked.add(num);
                int n = 1;
                int origin = num;
                while (numSet.contains(++num)) {
                    n += 1;
                    isChecked.add(num);
                }
                num = origin;
                while (numSet.contains(--num)) {
                    n += 1;
                    isChecked.add(num);
                }
                if (length < n) {
                    length = n;
                }
            }
        }
        return length;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        solution.longestConsecutive(new int[]{1,-8,7,-2,-4,-4,6,3,-4,0,-7,-1,5,1,-9,-3});
    }
}
