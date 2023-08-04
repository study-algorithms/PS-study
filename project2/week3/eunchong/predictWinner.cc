class Solution {
public:
    int search(vector<int>& nums, int start, int end, bool aTurn) {
        if (start > end)
            return 0;

        if (aTurn) {
            int aScore = nums[start] + search(nums, start+1, end, false);
            int bScore = nums[end] + search(nums, start, end-1, false);
            return max(aScore, bScore);
        } else {
            int aScore = search(nums, start+1, end, true);
            int bScore = search(nums, start, end-1, true);
            return min(aScore, bScore);
        }
    }

    bool predictTheWinner(vector<int>& nums) {
        int totalSum = 0;
        for (int & i: nums)
            totalSum += i;
        
        int maxSum = search(nums, 0, nums.size()-1, true);
        int minSum = totalSum - maxSum;

        return maxSum >= minSum;
    }
};
