class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        set<string> word_set(wordDict.begin(), wordDict.end());
        vector<int> dp(s.length(), -1);
        return wordBreakRecursion(s, word_set, 0, dp);
    }
    bool wordBreakRecursion(string s, set<string>& word_set, int start, vector<int>& dp) {
        if (start == s.length()) return true;

        if (dp[start] != -1) return dp[start];

        for (int end = start + 1; end <= s.length(); end++) {
            if (word_set.find(s.substr(start, end-start)) != word_set.end() 
                && wordBreakRecursion(s, word_set, end, dp))
                return dp[start] = true;
        }

        return dp[start] = false;
    }
};

/* 
Memoization + Recursion
1. From start point, check every end point of substring
2. If substring present and remaining string starting from end exists, return true
3. If no substring matches word_set, return false
*/
