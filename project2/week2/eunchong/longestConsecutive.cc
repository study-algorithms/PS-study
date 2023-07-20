class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> us(nums.begin(), nums.end()); // O(N)
        int count = 0;
        for (auto i : nums) { // O(N)
            if (us.find(i-1) == us.end()) {
                int j = i + 1;
                while (us.find(j) != us.end()) j++;
                count = max(count, j-i);
            }
        }
        return count;
    }
};

/*
Time Complexity O(N + N) = O(N)
Space Complexity O(N)
*/
