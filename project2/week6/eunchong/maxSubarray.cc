class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        if (nums.size() == 0) return 0;
        int curSum = 0, maxSum = INT_MIN;

        for (int i = 0; i < nums.size(); i++) {
            curSum += nums[i];
            curSum = max(curSum, nums[i]);
            maxSum = max(maxSum, curSum);
        }
        return maxSum;
    }
};
