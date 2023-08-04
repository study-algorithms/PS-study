class Solution {
public:
    int partitionString(string s) {
        unordered_set<char> us;
        int count = 1;

        for (char & c: s) {
            if (us.find(c) == us.end())
                us.insert(c);
            else {
                us.clear();
                us.insert(c);
                count++;
            }
        }
        return count;
    }
};
