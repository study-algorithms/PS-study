class Solution {
public:
    vector<vector<int>> intervalIntersection(vector<vector<int>>& firstList, vector<vector<int>>& secondList) {
        vector<vector<int>> result;
        int firstOne, firstTwo;
        for (int i = 0; i < firstList.size(); i++) {
            firstOne = firstList[i][0], firstTwo = firstList[i][1];
            for (int j = 0; j < secondList.size(); j++) {
                int secondOne = secondList[j][0], secondTwo = secondList[j][1];
                if ((firstOne >= secondOne && firstOne <= secondTwo) || (firstTwo >= secondOne && firstOne <= secondOne))
                    result.push_back({max(firstOne, secondOne), min(firstTwo, secondTwo)});
            }
        }
        return result;
    }
};
